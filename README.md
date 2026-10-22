# Learn Python — Beginner Course

An interactive, beginner-level Python course that runs entirely on your own
machine. Read a short lesson, type code in the exercise box, press **Submit**,
and get instant feedback on whether your output matches.

No accounts. No internet. No dependencies beyond Python itself.

## Run it

```bash
python3 server.py
```

Then open **http://127.0.0.1:8000**

Stop it with `ctrl+c`.

## What's inside

**39 lessons across 12 chapters:**

| # | Chapter | Lessons |
|---|---|---|
| 1 | Getting Started | Welcome to Python, `print()`, Comments, Errors Are Normal |
| 2 | Variables and Data | Variables, Numbers and Math, Strings, f-strings, Reading Numbers |
| 3 | Working with Strings | Splitting and Joining, Useful String Methods, Slicing |
| 4 | Making Decisions | Booleans, `if`/`else`, `elif` |
| 5 | Loops | `for` and `range`, `while`, `break`/`continue` |
| 6 | Loop Patterns | Nested Loops, `enumerate` and `zip`, List Comprehensions |
| 7 | Lists | Lists, Changing Lists, Looping Over Lists |
| 8 | Tuples and Sets | Tuples, Sets, Which One Do I Use? |
| 9 | Dictionaries | Dictionaries, Counting with a Dict, Looping Over a Dict |
| 10 | Functions | Functions, Parameters and `return`, Putting It Together |
| 11 | Handling Errors | `try`/`except`, Common Errors, Raising Your Own |
| 12 | Working with Files | Reading Files, Writing Files, Putting It Together |

Every lesson ends with a graded exercise.

The order is deliberate: strings are introduced before conditions, and
collection types come after you have looped over something. If you reorder
chapters, edit `CHAPTER_ORDER` in `content/build_lessons.py`.

## Features

- **Sidebar** with chapter grouping and live progress bar
- **Markdown lessons** — headings, tables, code blocks, callouts
- **Python syntax highlighting** — hand-written, no library
- **Exercise box** that runs your code and compares output to the expected answer
- **Progressive hints** — the Hint button reveals one nudge at a time, so you get
  unstuck without being handed the answer
- **Show solution** — a modal with one working solution, plus buttons to copy it
  or drop it into the editor
- **File exercises** — some lessons ship a real file (`notes.txt`, `sales.txt`)
  that your code reads; it appears in a panel above the editor
- **Progress saved** in `localStorage`, so it survives a refresh
- **Keyboard shortcuts** — `ctrl+,` back, `ctrl+.` next, `ctrl+enter` submit,
  `ctrl+h` hint, `esc` close modal
- Works on mobile (sidebar collapses)

## Files

```
index.html                  lesson player shell
app.js                      sidebar, markdown renderer, highlighter, code checks
style.css                   dark theme
server.py                   static server + code-check API (stdlib only)
content/lessons.json        the lessons
content/build_lessons.py    lesson source + self-test generator
content/e2e_test.py         API test of the running server
tests/dom.test.mjs          browser test (clicks the real buttons)
tests/run.sh                runs everything
package.json                dev-only; happy-dom for the browser test
```

The app has **zero runtime dependencies**. `package.json` exists only so the
browser test can pull in `happy-dom`; nothing in `index.html`, `app.js` or
`server.py` needs it.

## Adding or editing lessons

Lessons are authored in `content/build_lessons.py` as plain markdown, then
compiled to JSON. Each lesson has an optional exercise with an `expected` output
and, for file lessons, a `files` map of pre-existing file contents:

```python
lesson("reading", "Working with Files", "Reading Files", """
# Reading Files
...markdown...
""", {
    "prompt": "Read notes.txt and print its contents.",
    "starter": "",
    "expected": "hello",
    "files": {"notes.txt": "hello\n"},
}, 'with open("notes.txt") as f:\n    print(f.read().strip())')
```

Hints live in a separate `HINTS` dict keyed by lesson id. Each entry is a list
revealed one at a time, so the first nudge stays a nudge:

```python
HINTS = {
    "reading": [
        "The file already exists -- check the panel above the code box.",
        "Use a with block around open(), then print what .read() returns.",
    ],
}
```

The reference solution you pass to `lesson()` becomes the code shown by
**Show solution**, so it has to be correct — the build checks that it is.

```bash
python3 content/build_lessons.py
```

That command **verifies every reference solution** — it runs each one in a
throwaway directory with its files seeded, and confirms the output matches what
the exercise expects. It also fails if any lesson is missing hints. If you edit
a lesson and break its solution, the build tells you which one.

## Testing

One command, from the repo root:

```bash
./tests/run.sh
```

It builds the lessons (which verifies every reference solution), starts a
server, runs the API tests, runs the browser tests, and shuts the server down.

To run the pieces separately, with `python3 server.py` already running:

```bash
python3 content/e2e_test.py        # API + execution safety
bun tests/dom.test.mjs             # browser behaviour
```

The API test submits every lesson's solution through the real HTTP API,
confirms wrong answers are rejected, checks that each published solution passes
its own exercise, and verifies that infinite loops are killed, output is capped,
file scenarios behave, and path traversal is refused.

The browser test loads the real `index.html` and `app.js` in a headless DOM and
clicks the actual buttons: hints reveal one at a time, the solution modal opens,
fills the editor and closes, submitting the published solution passes, wrong
answers are rejected, navigating resets per-lesson state, and the keyboard
shortcuts work. It needs `bun` and a one-time `bun install`; without either,
`run.sh` skips it and says so.

## ⚠️ Security

`/api/run` and `/api/check` **execute Python code submitted over HTTP**.

That is arbitrary code execution. It is safe here only because:

- the server binds to `127.0.0.1` (localhost, not your network)
- each snippet runs in its own process, with a **fresh temporary working
  directory** as its cwd, a 5-second timeout, and an 8 KB output cap
- file paths supplied with an exercise are validated — absolute paths and `..`
  are refused

None of that is a real sandbox. A snippet can still read any file your user can
read, and can reach the network. The temp directory controls where *lesson
files* land; it does not confine malicious code.

**Do not deploy this to a public server as-is.** If you want to host it, run
student code inside a disposable container with no network access and a mounted
read-only filesystem.
