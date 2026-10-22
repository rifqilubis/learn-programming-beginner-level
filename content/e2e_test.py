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

fails = []
for lesson in lessons:
    ex = lesson.get("exercise")
    if not ex:
        continue
    sol = solutions.get(lesson["id"])
    if sol is None:
        fails.append((lesson["id"], "no reference solution"))
        continue

    # correct solution must pass
    r = post("/api/check", {"code": sol, "expected": ex["expected"]})
    if not r.get("passed"):
        fails.append((lesson["id"], f"solution failed: {r}"))

    # wrong solution must NOT pass
    r2 = post("/api/check", {"code": "print('definitely wrong')", "expected": ex["expected"]})
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

if fails:
    for name, why in fails:
        print(f"FAIL {name}: {why}")
    sys.exit(1)

print(f"PASS: {len(lessons)} lessons, {sum(1 for l in lessons if l.get('exercise'))} exercises")
print("PASS: wrong answers rejected")
print("PASS: infinite loop killed, output capped, hard-exit survived")
