#!/usr/bin/env bash
# Runs every test: content build verification, API tests, and browser tests.
# Starts its own server and shuts it down afterwards.
set -uo pipefail

cd "$(dirname "$0")/.."
PORT=8000
FAIL=0

cleanup() {
  [ -n "${SERVER_PID:-}" ] && kill "$SERVER_PID" 2>/dev/null
  wait "$SERVER_PID" 2>/dev/null
}
trap cleanup EXIT

echo "==> building lessons (verifies every reference solution)"
python3 content/build_lessons.py || FAIL=1

echo
echo "==> starting server"
python3 server.py >/tmp/learn-python-test.log 2>&1 &
SERVER_PID=$!
for _ in $(seq 1 40); do
  curl -sf -o /dev/null "http://127.0.0.1:$PORT/api/lessons" && break
  sleep 0.25
done

echo
echo "==> API tests"
python3 content/e2e_test.py || FAIL=1

echo
if command -v bun >/dev/null 2>&1 && [ -d node_modules/happy-dom ]; then
  echo "==> browser tests (bun + happy-dom)"
  bun tests/dom.test.mjs || FAIL=1
else
  echo "==> browser tests SKIPPED"
  echo "    install bun, then:  bun install"
fi

echo
if [ "$FAIL" -eq 0 ]; then
  echo "ALL TESTS PASSED"
else
  echo "SOME TESTS FAILED"
fi
exit "$FAIL"
