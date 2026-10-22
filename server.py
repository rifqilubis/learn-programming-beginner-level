#!/usr/bin/env python3
"""Zero-dependency lesson server for the Python beginner course.

    python3 server.py            # then open http://127.0.0.1:8000

SAFETY: /api/run executes the Python code typed into the exercise box.
It is bound to localhost, runs in an isolated subprocess with a timeout and an
output cap -- but that is NOT a real sandbox. Do not expose this to the
internet. For a public version, run student code inside a container with no
network access.
"""

import json
import subprocess
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TIMEOUT_SECONDS = 5
MAX_OUTPUT = 8000
HOST = "127.0.0.1"
PORT = 8000


def run_python(code: str) -> dict:
    """Run a snippet in a fresh isolated interpreter and capture its output."""
    try:
        proc = subprocess.run(
            [sys.executable, "-I", "-c", code],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return {
            "ok": False,
            "stdout": "",
            "stderr": f"Timed out after {TIMEOUT_SECONDS}s. Infinite loop?",
        }

    return {
        "ok": proc.returncode == 0,
        "stdout": proc.stdout[:MAX_OUTPUT],
        "stderr": proc.stderr[:MAX_OUTPUT],
    }


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
            code = self._read_body().get("code", "")
            if not isinstance(code, str):
                self._send_json({"error": "code must be a string"}, status=400)
                return
            self._send_json(run_python(code))
            return

        if self.path == "/api/check":
            payload = self._read_body()
            code = payload.get("code", "")
            expected = payload.get("expected", "")
            if not isinstance(code, str) or not isinstance(expected, str):
                self._send_json({"error": "code and expected must be strings"}, status=400)
                return
            result = run_python(code)
            result["passed"] = result["ok"] and normalize(result["stdout"]) == normalize(expected)
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
