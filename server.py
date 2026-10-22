#!/usr/bin/env python3
"""Zero-dependency lesson server for the Python beginner course.

    python3 server.py            # then open http://127.0.0.1:8000

SAFETY: /api/run executes the Python code typed into the exercise box.
It is bound to localhost, runs in an isolated subprocess with a timeout and an
output cap -- but that is NOT a real sandbox. Do not expose this to the
internet. For a public version, run student code inside a container with no
network access.

HOW STUDENT CODE RUNS: the snippet is written to main.py inside a throwaway
directory and run as `python3 -E -s main.py`.

  -E  ignore PYTHONPATH and other PYTHON* environment variables
  -s  do not add the user's site-packages directory

We deliberately do NOT use -I. It would also strip the script's own directory
from sys.path, which breaks two things a beginner course needs: `import` of a
file the student just wrote, and tracebacks that point at the real line in
their own code. -E -s keeps the isolation that matters here while letting
lessons teach modules and error messages honestly.
"""

import json
import shutil
import subprocess
import sys
import tempfile
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent
TIMEOUT_SECONDS = 5
MAX_OUTPUT = 8000
HOST = "127.0.0.1"
PORT = 8000

# Student code is written to this file in the temp dir. Lessons that teach
# imports should not seed a file with this name, or the snippet wins and the
# lesson's own file is overwritten.
MAIN_FILE = "main.py"


def safe_files(files) -> dict:
    """Keep only plain relative paths, so a lesson cannot seed files outside its temp dir."""
    if not isinstance(files, dict):
        return {}
    clean = {}
    for name, content in files.items():
        if not isinstance(name, str) or not isinstance(content, str):
            continue
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or not name.strip():
            continue
        clean[name] = content
    return clean


def name_error(returncode: int, stderr: str) -> str:
    """Explain a non-zero exit, including the common `os._exit` failure.

    A snippet that calls sys.exit()/os._exit() before printing leaves the
    student staring at silent output, so this names the cause instead.
    """
    if returncode > 0:
        # Uncaught exception: Python already printed the traceback. Point at
        # the last line, which is the actual error type and message.
        lines = [line for line in stderr.strip().splitlines() if line.strip()]
        if lines:
            return lines[-1].strip()
        return f"The program stopped with exit code {returncode}."
    if returncode < 0:
        return (f"The program was killed by signal {-returncode}. A call like "
                f"os._exit() or an infinite loop can do this.")
    return ""


def run_python(code: str, files=None) -> dict:
    """Run a snippet in a fresh interpreter, inside a throwaway directory.

    Each run gets its own temp cwd, so file lessons can write and read freely
    without touching the repo. `files` seeds the directory beforehand.
    """
    workdir = tempfile.mkdtemp(prefix="lesson-")
    try:
        for name, content in safe_files(files).items():
            target = Path(workdir, name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")

        # Run from a file rather than -c so tracebacks and `import` both point
        # at the student's own directory. See the module docstring.
        script = Path(workdir, MAIN_FILE)
        script.write_text(code, encoding="utf-8")

        try:
            proc = subprocess.run(
                [sys.executable, "-E", "-s", MAIN_FILE],
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                cwd=workdir,
            )
        except subprocess.TimeoutExpired:
            return {
                "ok": False,
                "stdout": "",
                "stderr": f"Timed out after {TIMEOUT_SECONDS}s. Infinite loop?",
            }
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    return {
        "ok": proc.returncode == 0,
        "stdout": proc.stdout[:MAX_OUTPUT],
        "stderr": clean_stderr(proc.stderr, workdir)[:MAX_OUTPUT],
        "error": name_error(proc.returncode, proc.stderr),
    }


def clean_stderr(stderr: str, workdir: str) -> str:
    """Hide the throwaway directory so tracebacks name the student's own file.

    Without this a beginner sees File "/tmp/lesson-c69ap7wl/main.py", line 3,
    which reads like someone else's problem. The line number is what matters.
    """
    return stderr.replace(workdir.rstrip("/") + "/", "")


def normalize(text: str) -> str:
    """Compare output ignoring trailing whitespace on each line."""
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
    return "\n".join(lines).strip("\n")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))

    def _send_json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self) -> dict:
        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0:
            return {}
        try:
            return json.loads(self.rfile.read(length).decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            return {}

    def do_GET(self):
        if self.path == "/api/lessons":
            try:
                data = json.loads((ROOT / "content" / "lessons.json").read_text("utf-8"))
            except OSError as exc:
                self._send_json({"error": str(exc)}, status=500)
                return
            self._send_json(data)
            return
        super().do_GET()

    def do_POST(self):
        if self.path == "/api/run":
            payload = self._read_body()
            code = payload.get("code", "")
            if not isinstance(code, str):
                self._send_json({"error": "code must be a string"}, status=400)
                return
            self._send_json(run_python(code, payload.get("files")))
            return

        if self.path == "/api/check":
            payload = self._read_body()
            code = payload.get("code", "")
            expected = payload.get("expected", "")
            if not isinstance(code, str) or not isinstance(expected, str):
                self._send_json({"error": "code and expected must be strings"}, status=400)
                return
            result = run_python(code, payload.get("files"))
            result["passed"] = result["ok"] and normalize(result["stdout"]) == normalize(expected)
            if not result["passed"]:
                # Say *why* when the program died, so "Not quite" is not the
                # only feedback a beginner gets.
                if not result["ok"] and result.get("error"):
                    result["reason"] = result["error"]
                elif not result["ok"]:
                    result["reason"] = "The program exited without finishing."
                else:
                    result["reason"] = "The output did not match what the exercise asked for."
            self._send_json(result)
            return

        self._send_json({"error": "not found"}, status=404)


def main() -> None:
    if not (ROOT / "content" / "lessons.json").exists():
        sys.exit("content/lessons.json is missing -- run this from the repo root.")
    print(f"Python course running at http://{HOST}:{PORT}  (ctrl+c to stop)")
    print("Note: student code runs locally, unsandboxed. Localhost only.\n")
    try:
        ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
