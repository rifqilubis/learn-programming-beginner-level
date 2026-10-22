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

**30 lessons across 9 chapters:**

| Chapter | Lessons |
|---|---|
| Getting Started | Welcome to Python, `print()`, Comments, Errors Are Normal |
| Variables and Data | Variables, Numbers and Math, Strings, f-strings, Reading Numbers |
| Making Decisions | Booleans, `if`/`else`, `elif` |
| Loops | `for` and `range`, `while`, `break`/`continue` |
| Lists | Lists, Changing Lists, Looping Over Lists |
| Functions | Functions, Parameters and `return`, Putting It Together |
| Dictionaries | Dictionaries, Counting with a Dict, Looping Over a Dict |
| Handling Errors | `try`/`except`, Common Errors, Raising Your Own |
| Working with Files | Reading Files, Writing Files, Putting It Together |

Every lesson ends with a graded exercise.

## Features

- **Sidebar** with chapter grouping and live progress bar
- **Markdown lessons** — headings, tables, code blocks, callouts
- **Python syntax highlighting** — hand-written, no library
- **Exercise box** that runs your code and compares output to the expected answer
- **File exercises** — some lessons ship a real file (`notes.txt`, `sales.txt`)
  that your code reads; it appears in a panel above the editor
- **Progress saved** in `localStorage`, so it survives a refresh
- **Keyboard shortcuts** — `ctrl+,` back, `ctrl+.` next, `ctrl+enter` submit
- Works on mobile (sidebar collapses)

## Files

```
index.html                  lesson player shell
app.js                      sidebar, markdown renderer, highlighter, code checks
style.css                   dark theme
server.py                   static server + code-check API (stdlib only)
content/lessons.json        the lessons
content/build_lessons.py    lesson source + self-test generator
content/e2e_test.py         end-to-end test of the running server
```

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

```bash
python3 content/build_lessons.py
```

That command **verifies every reference solution** — it runs each one in a
throwaway directory with its files seeded, and confirms the output matches what
the exercise expects. If you edit a lesson and break its solution, the build
fails and tells you which one.

## Testing

With the server running:

```bash
python3 content/e2e_test.py
```

It submits every lesson's solution through the real HTTP API, confirms wrong
answers are rejected, and checks that infinite loops are killed, output is
capped, file scenarios behave, and path traversal is refused.

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
