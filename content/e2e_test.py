#!/usr/bin/env python3
"""End-to-end test: drives the running server exactly like the browser does."""
import json
import sys
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:8000"


def post(path, payload):
    req = urllib.request.Request(
        BASE + path,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.load(res)


def get(path):
    with urllib.request.urlopen(BASE + path, timeout=30) as res:
        return json.load(res)


sys.path.insert(0, "content")
import build_lessons as B  # noqa: E402  (reference solutions live here)

lessons = get("/api/lessons")["lessons"]
solutions = {i: sol for i, _c, _t, _b, _e, sol in B.L if sol}
exercises = {i: ex for i, _c, _t, _b, ex, _s in B.L if ex}

fails = []
for lesson in lessons:
    ex = lesson.get("exercise")
    if not ex:
        continue
    sol = solutions.get(lesson["id"])
    if sol is None:
        fails.append((lesson["id"], "no reference solution"))
        continue

    files = ex.get("files") or {}

    # correct solution must pass
    r = post("/api/check", {"code": sol, "expected": ex["expected"], "files": files})
    if not r.get("passed"):
        fails.append((lesson["id"], f"solution failed: {r}"))

    # wrong solution must NOT pass
    r2 = post("/api/check", {"code": "print('definitely wrong')",
                             "expected": ex["expected"], "files": files})
    if r2.get("passed"):
        fails.append((lesson["id"], "wrong answer was accepted"))

# edge cases
r = post("/api/run", {"code": "while True: pass"})
if r.get("ok") or "Timed out" not in r.get("stderr", ""):
    fails.append(("timeout", f"infinite loop not killed: {r}"))

r = post("/api/check", {"code": "print('a')\n", "expected": "a"})
if not r.get("passed"):
    fails.append(("trailing-newline", f"trailing newline not tolerated: {r}"))

r = post("/api/run", {"code": "print('x'*100000)"})
if len(r.get("stdout", "")) > 8000:
    fails.append(("output-cap", "output cap not enforced"))

r = post("/api/run", {"code": "import os; os._exit(0)"})
if r.get("ok") is None:
    fails.append(("crash-resilience", f"server died on hard exit: {r}"))

# --- file isolation: seeded files must be readable, and writes must not leak ---
r = post("/api/run", {"code": 'print(open("d.txt").read().strip())', "files": {"d.txt": "seeded\n"}})
if r.get("stdout", "").strip() != "seeded":
    fails.append(("seed-file", f"seeded file not readable: {r}"))

r = post("/api/run", {"code": 'open("leak.txt","w").write("x"); print("wrote")'})
if r.get("stdout", "").strip() != "wrote":
    fails.append(("write-file", f"could not write in temp dir: {r}"))

r = post("/api/run", {"code": 'import os; print(os.path.exists("leak.txt"))'})
if r.get("stdout", "").strip() != "False":
    fails.append(("temp-isolation", "files leaked between runs"))

r = post("/api/run", {"code": 'import os; print(os.getcwd())'})
if "/tmp/lesson-" not in r.get("stdout", ""):
    fails.append(("cwd", f"not running in a temp dir: {r.get('stdout')!r}"))

# --- path traversal in the files map must be refused ---
r = post("/api/run", {"code": 'import os; print(os.path.exists("../../escape.txt"))',
                      "files": {"../../escape.txt": "bad"}})
if r.get("stdout", "").strip() != "False":
    fails.append(("traversal", f"path traversal was allowed: {r}"))

# --- nested file paths are still supported ---
r = post("/api/run", {"code": 'print(open("sub/x.txt").read().strip())', "files": {"sub/x.txt": "deep\n"}})
if r.get("stdout", "").strip() != "deep":
    fails.append(("nested-file", f"nested seed failed: {r}"))

# --- students must be able to import a file they wrote (needs cwd on sys.path) ---
r = post("/api/run", {"code": "import helper\nprint(helper.VALUE)",
                      "files": {"helper.py": "VALUE = 42\n"}})
if r.get("stdout", "").strip() != "42":
    fails.append(("local-import", f"could not import a seeded module: {r}"))

# --- tracebacks must name the student's file and a real line number ---
r = post("/api/run", {"code": "print(1)\nprint(2)\nprint(1/0)"})
stderr = r.get("stderr", "")
if 'File "main.py", line 3' not in stderr:
    fails.append(("traceback-line", f"traceback lacks main.py line 3: {stderr!r}"))
if "/tmp/lesson-" in stderr:
    fails.append(("traceback-path", f"temp dir leaked into traceback: {stderr!r}"))
if r.get("error") != "ZeroDivisionError: division by zero":
    fails.append(("traceback-error", f"error field wrong: {r.get('error')!r}"))

# --- a failed check must explain itself, not just say "not quite" ---
r = post("/api/check", {"code": "print(1/0)", "expected": "3"})
if r.get("passed") is not False:
    fails.append(("check-reason", "a crashing program must not pass"))
if "ZeroDivisionError" not in (r.get("reason") or ""):
    fails.append(("check-reason", f"no reason given for failure: {r}"))

# --- PYTHONPATH must be ignored (-E), or a lesson could be hijacked by env ---
r = post("/api/run", {"code": "import sys; print('/tmp/evil' in sys.path)"})
if r.get("stdout", "").strip() != "False":
    fails.append(("env-isolation", f"PYTHONPATH-style paths present: {r.get('stdout')!r}"))

# --- exercises must not interpret the runner's own main.py as a lesson file ---
r = post("/api/run", {"code": 'print(open("main.py").read()[:6])'})
if r.get("stdout", "").strip() != "print(":
    fails.append(("main-file", f"student code is not main.py: {r}"))

# --- every published solution must be correct and pass its own exercise ---
for lesson in lessons:
    ex = lesson.get("exercise")
    if not ex:
        continue
    sol = ex.get("solution")
    if not sol:
        fails.append((lesson["id"], "no solution published"))
        continue
    r = post("/api/check", {"code": sol, "expected": ex["expected"], "files": ex.get("files") or {}})
    if not r.get("passed"):
        fails.append((lesson["id"], f"published solution fails its own exercise: {r}"))
    if not ex.get("hints"):
        fails.append((lesson["id"], "no hints published"))

if fails:
    for name, why in fails:
        print(f"FAIL {name}: {why}")
    sys.exit(1)

print(f"PASS: {len(lessons)} lessons, {sum(1 for l in lessons if l.get('exercise'))} exercises")
print("PASS: wrong answers rejected")
print("PASS: infinite loop killed, output capped, hard-exit survived")
print("PASS: file seeding, temp-dir isolation, no leaks between runs")
print("PASS: path traversal refused, nested paths allowed")
print("PASS: local module imports work, tracebacks name the student's own line")
print("PASS: failed checks explain why, PYTHONPATH ignored")
print("PASS: every published solution passes, every exercise has hints")
