#!/usr/bin/env python3
"""One-shot generator for content/lessons.json. Not shipped in the repo."""
import json
from pathlib import Path

L = []  # (id, chapter, title, body, exercise|None, solution|None)


def lesson(id, chapter, title, body, exercise=None, solution=None):
    L.append((id, chapter, title, body.strip(), exercise, solution))


# ---------------------------------------------------------------- ch1
lesson("welcome", "Getting Started", "Welcome to Python", """
# Welcome to Python

Python is a programming language. You write instructions in a file, and Python
runs them from top to bottom, one line at a time.

It is a good first language because the code looks close to English:

```python
print("Hello, world!")
```

That single line prints text to the screen. Compare it to languages where the
same task needs five lines of setup, and you can see why beginners start here.

## How this course works

- Each lesson is short. Read it, then do the **Assignment** at the bottom.
- Type your code in the box and press **Submit**.
- If it is wrong, you get the expected output next to yours. Compare them.
- Press **ctrl+.** or the **Next** button to continue.

> You cannot break anything. Every exercise runs in its own throwaway Python
> process, so a crash costs you nothing.
""", {
    "prompt": "Print exactly: Hello, world!",
    "starter": "# Type your code below\n",
    "expected": "Hello, world!",
}, 'print("Hello, world!")')

lesson("print", "Getting Started", "print()", """
# print()

`print()` shows something on the screen. Whatever you put inside the
parentheses is what appears in the output.

```python
print("Python is fun")
```

The quotes are **not** printed. They tell Python "everything between these is
text, not code."

## Printing more than once

Python runs line by line, so each `print()` starts a new line:

```python
print("one")
print("two")
```

```
one
two
```

## Numbers vs text

Text needs quotes. Numbers do not:

```python
print("7")   # prints 7
print(7)     # prints 7
print(7 + 1) # prints 8, because it is math
```

The first one is the *text* `7`. The last one is *math*, so Python calculates
it. If you put quotes around math, it stays text: `print("7 + 1")` prints
exactly `7 + 1`.
""", {
    "prompt": "Print three lines: Python, is, awesome",
    "starter": 'print("Python")\n',
    "expected": "Python\nis\nawesome",
}, 'print("Python")\nprint("is")\nprint("awesome")')

lesson("comments", "Getting Started", "Comments", """
# Comments

A comment is a note for humans. Python ignores it completely.

```python
# This line does nothing
print("but this line runs")   # comments can go at the end too
```

Anything after a `#` on a line is a comment.

## Why bother?

Because code tells you *what* it does, and never *why*. Six months from now you
will read your own code and wonder why you did something. A short comment saves
you.

```python
# Tax rate is 11% for this country, not the usual 10%
tax = 0.11
```

That comment carries information the code cannot.

> **Don't** narrate the obvious. `# increment x by 1` above `x = x + 1` is noise.
> Explain the reason, not the action.
""", {
    "prompt": "Add a comment on the first line, then print: done",
    "starter": "# write your comment here\n",
    "expected": "done",
}, '# a comment\nprint("done")')

lesson("errors", "Getting Started", "Errors Are Normal", """
# Errors Are Normal

Every programmer sees errors all day. They are not punishment, they are Python
telling you where it got confused.

```python
print("hello"
```

```
SyntaxError: '(' was never closed
```

Python read the line, noticed the opening `(` was never closed, and stopped.
The fix is a `)`.

## Reading an error message

Errors are written **bottom up**. The last line is the most important -- it is
the actual problem. The lines above it are the trail of *where* it happened.

A very common one:

```python
print(greeting)
```

```
NameError: name 'greeting' is not defined
```

Python is saying: "you used a name I have never been told about." Usually it is
a typo, or you forgot to create the variable first.

> When you hit an error, read the **last line first**, then look at the line
> number Python gives you.
""", {
    "prompt": "This code has a mistake. Fix it so it prints: fixed",
    "starter": 'print("fixed"\n',
    "expected": "fixed",
}, 'print("fixed")')

# ---------------------------------------------------------------- ch2
lesson("variables", "Variables and Data", "Variables", """
# Variables

A variable is a name pointing at a value. You create one with `=`.

```python
name = "Ada"
age = 36
print(name)
```

```
Ada
```

`=` means "store this on the right into the name on the left." It is **not**
"equals" like in math. That is why this works:

```python
score = 10
score = score + 5   # take score, add 5, store it back
print(score)        # 15
```

Read that as: *look up score (10), add 5, put the result back into score.*

## Naming rules

- Letters, numbers and underscores only. No spaces.
- Cannot start with a number. `2fast` is invalid, `fast2` is fine.
- Case matters: `Name` and `name` are two different variables.

Good names describe the value: `user_count` beats `x`. You will read the name
far more often than you type it.
""", {
    "prompt": "Create a variable `city` set to Tokyo, then print it.",
    "starter": "",
    "expected": "Tokyo",
}, 'city = "Tokyo"\nprint(city)')

lesson("numbers", "Variables and Data", "Numbers and Math", """
# Numbers and Math

Python does arithmetic with the symbols you already know:

| Symbol | Meaning | Example | Result |
|---|---|---|---|
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide | `7 / 2` | `3.5` |
| `//` | divide, drop remainder | `7 // 2` | `3` |
| `%` | remainder | `7 % 2` | `1` |
| `**` | power | `7 ** 2` | `49` |

## Two kinds of number

- **int** -- whole numbers: `1`, `42`, `-7`
- **float** -- decimals: `3.5`, `0.1`

Division with `/` **always** gives a float, even when it divides evenly:
`10 / 2` is `5.0`, not `5`. Use `//` when you want a whole number.

## Order of operations

Same as maths: `*` and `/` happen before `+` and `-`. Use parentheses to be
explicit.

```python
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20
```
""", {
    "prompt": "Print the result of 17 divided by 5 using the // operator (whole-number division).",
    "starter": "",
    "expected": "3",
}, 'print(17 // 5)')

lesson("strings", "Variables and Data", "Strings", """
# Strings

A string is text. It goes in quotes -- single `'` or double `"` both work.

```python
first = "Grace"
last = 'Hopper'
```

## Joining strings

`+` sticks strings together:

```python
full = first + " " + last
print(full)   # Grace Hopper
```

You cannot add a string to a number. This is an error:

```python
print("age: " + 36)   # TypeError
```

That is Python protecting you from producing nonsense. Convert first with
`str()`:

```python
print("age: " + str(36))   # age: 36
```

## Useful string methods

Methods are actions attached to a value with a dot.

```python
word = "Python"
print(word.upper())      # PYTHON
print(word.lower())      # python
print(len(word))         # 6
print(word[0])           # P
```

`len()` counts characters. `word[0]` takes the **first** character -- counting
starts at 0, not 1. That trips up everyone once; you will get used to it.
""", {
    "prompt": "Take the string `greeting = \"hello\"` and print it in uppercase.",
    "starter": 'greeting = "hello"\n',
    "expected": "HELLO",
}, 'greeting = "hello"\nprint(greeting.upper())')

lesson("fstrings", "Variables and Data", "f-strings", """
# f-strings

Building strings with `+` and `str()` gets ugly fast. An f-string is cleaner:
put an `f` before the quote and wrap variables in curly braces.

```python
name = "Ada"
age = 36
print(f"{name} is {age} years old")
```

```
Ada is 36 years old
```

Inside the braces Python runs real code, so you can calculate:

```python
price = 20
print(f"Total: {price * 1.1}")
```

```
Total: 22.0
```

## Formatting numbers

Decimals can be messy: `22.000000000000004`. Control them with `:.2f`, meaning
"two digits after the point":

```python
print(f"Total: {price * 1.1:.2f}")
```

```
Total: 22.00
```

> This is the single most useful formatting trick in Python. Reach for it
> whenever you print money.
""", {
    "prompt": "Set item = \"coffee\" and cost = 3, then print: coffee costs 3 dollars",
    "starter": 'item = "coffee"\ncost = 3\n',
    "expected": "coffee costs 3 dollars",
}, 'item = "coffee"\ncost = 3\nprint(f"{item} costs {cost} dollars")')

lesson("input", "Variables and Data", "Reading Numbers", """
# Reading Numbers

The exercise box gives you no keyboard input, so we practice the part that
actually trips people up: **converting types**.

`input()` always returns a **string**, even when the user types `42`. So this
is a bug:

```python
age = input("Age: ")   # "42", a string
print(age + 1)         # TypeError
```

Fix it by converting with `int()`:

```python
age = int(input("Age: "))
print(age + 1)
```

## The two converters

```python
int("42")     # 42      text to whole number
float("3.5")  # 3.5     text to decimal
str(42)       # "42"    number to text
```

If the text is not a number, `int()` raises `ValueError`. That is expected --
real programs check for it.
""", {
    "prompt": "The text \\\"8\\\" needs to become a number. Set n = 8 by converting the string, then print n + 2",
    "starter": 'n = "8"\n',
    "expected": "10",
}, 'n = int("8")\nprint(n + 2)')

# ---------------------------------------------------------------- ch3
lesson("booleans", "Making Decisions", "Booleans", """
# Booleans

A boolean is either `True` or `False`. Note the capital letters -- `true` is
not valid Python.

You rarely type booleans directly. You get them from comparisons:

```python
print(5 > 3)     # True
print(5 < 3)     # False
print(5 == 3)    # False
print(5 != 3)    # True
```

⚠️ `==` compares. `=` assigns. Mixing these up is the most common beginner bug.

```python
x = 5     # store 5 in x
x == 5    # ask: is x equal to 5?
```

## Combining conditions

`and`, `or`, `not`:

```python
age = 20
has_ticket = True

print(age >= 18 and has_ticket)   # True
print(age < 18 or has_ticket)     # True
print(not has_ticket)             # False
```

- `and` -- both must be true
- `or` -- at least one must be true
- `not` -- flips it
""", {
    "prompt": "Print the result of checking whether 10 is greater than 3.",
    "starter": "",
    "expected": "True",
}, 'print(10 > 3)')

lesson("if", "Making Decisions", "if and else", """
# if and else

`if` runs code only when a condition is true.

```python
temperature = 30

if temperature > 25:
    print("hot")
```

```
hot
```

## Indentation is the syntax

The four spaces before `print` are not decoration -- they are how Python knows
which lines belong inside the `if`. Every line indented the same amount is part
of the same block.

```python
if temperature > 25:
    print("hot")
    print("wear shorts")
print("done")          # not indented, so always runs
```

## else

`else` covers "everything other than the if":

```python
if temperature > 25:
    print("hot")
else:
    print("not hot")
```

Exactly one of the two branches runs. Never both.
""", {
    "prompt": "Set score = 75. If score is 60 or more, print pass, otherwise print fail.",
    "starter": "score = 75\n",
    "expected": "pass",
}, 'score = 75\nif score >= 60:\n    print("pass")\nelse:\n    print("fail")')

lesson("elif", "Making Decisions", "elif", """
# elif

`elif` means "else, if". It lets you check several conditions in order and stop
at the first one that matches.

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

```
B
```

## Order matters

Python checks top to bottom and stops at the **first** true condition. Because
of that, `score >= 80` was enough -- we did not need `80 <= score < 90`.

Reversing the order breaks it:

```python
if score >= 70:
    print("C")
elif score >= 90:
    print("A")    # never reached: 85 already matched >= 70
```

Write conditions from most specific to least.

> One `if` chain runs **at most one** branch. If you want several independent
> checks, use separate `if` statements instead.
""", {
    "prompt": "Set n = 0. Print positive if n > 0, negative if n < 0, otherwise print zero.",
    "starter": "n = 0\n",
    "expected": "zero",
}, 'n = 0\nif n > 0:\n    print("positive")\nelif n < 0:\n    print("negative")\nelse:\n    print("zero")')

# ---------------------------------------------------------------- ch4
lesson("for", "Loops", "for and range", """
# for and range

A loop repeats code. `for` repeats once for each item in a sequence.

```python
for i in range(3):
    print(i)
```

```
0
1
2
```

`range(3)` produces `0, 1, 2`. It starts at 0 and stops **before** 3. That
"stops before" is consistent everywhere in Python and worth memorising.

## Counting from 1

```python
for i in range(1, 4):
    print(i)
```

```
1
2
3
```

`range(start, stop)` -- start included, stop excluded.

## Looping over text

```python
for letter in "abc":
    print(letter)
```

```
a
b
c
```

The variable name (`i`, `letter`) is yours to choose. Pick something that says
what one item is.
""", {
    "prompt": "Print the numbers 1 to 4, one per line, using a for loop.",
    "starter": "",
    "expected": "1\n2\n3\n4",
}, 'for i in range(1, 5):\n    print(i)')

lesson("while", "Loops", "while", """
# while

`while` repeats **as long as** a condition stays true. Use it when you do not
know in advance how many times you need to loop.

```python
count = 0
while count < 3:
    print(count)
    count = count + 1
```

```
0
1
2
```

## The line that changes the condition

Look at `count = count + 1`. Without it, `count` stays `0`, the condition stays
true, and the loop never ends -- an **infinite loop**. Your program hangs and
you Ctrl+C to escape.

Every `while` loop needs something inside it that eventually makes the
condition false. If you write a `while` and it hangs, that is the first thing to
check.

> The exercise box kills any program after 5 seconds, so an accidental infinite
> loop here costs you a few seconds and a timeout message.
""", {
    "prompt": "Use a while loop to print the numbers 3, 2, 1 (counting down).",
    "starter": "n = 3\n",
    "expected": "3\n2\n1",
}, 'n = 3\nwhile n > 0:\n    print(n)\n    n = n - 1')

lesson("break", "Loops", "break and continue", """
# break and continue

Two words change how a loop behaves from inside.

**`break`** leaves the loop immediately:

```python
for i in range(10):
    if i == 3:
        break
    print(i)
```

```
0
1
2
```

**`continue`** skips the rest of this round and goes to the next:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

```
0
1
3
4
```

## Which one?

- `break` -- "I found what I needed, stop looking."
- `continue` -- "Not this one, skip to the next."

> Use them sparingly. A loop with three `break`s is hard to follow. Often an
> `if` around the work does the same thing more clearly.
""", {
    "prompt": "Loop 1 to 10, but stop (break) as soon as you reach 4. Print each number before checking.",
    "starter": "",
    "expected": "1\n2\n3",
}, 'for i in range(1, 11):\n    if i == 4:\n        break\n    print(i)')

# ---------------------------------------------------------------- ch5
lesson("lists", "Lists", "Lists", """
# Lists

A list holds many values in order, in one variable. Square brackets, items
separated by commas.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

```
['apple', 'banana', 'cherry']
```

## Getting one item out

Indexing starts at **0**, so the first item is `fruits[0]`:

```python
print(fruits[0])    # apple
print(fruits[2])    # cherry
```

Negative numbers count from the end, which is handy:

```python
print(fruits[-1])   # cherry
```

## Leaving one out

Useful when you read indices out loud as "from 0, up to but not including 2":

```python
print(fruits[0:2])   # ['apple', 'banana']
```

## How many?

```python
print(len(fruits))   # 3
```

> Lists can hold any mix of types, including other lists. They are far more
> flexible than arrays in older languages.
""", {
    "prompt": "From colors = [\"red\", \"green\", \"blue\"], print the second item (green).",
    "starter": 'colors = ["red", "green", "blue"]\n',
    "expected": "green",
}, 'colors = ["red", "green", "blue"]\nprint(colors[1])')

lesson("listops", "Lists", "Changing Lists", """
# Changing Lists

Lists are **mutable** -- you can change them after creating them.

## Add to the end

```python
tasks = ["write", "test"]
tasks.append("ship")
print(tasks)
```

```
['write', 'test', 'ship']
```

## Replace an item

Assign to an index:

```python
tasks[0] = "draft"
print(tasks[0])    # draft
```

## Remove

```python
tasks.remove("test")   # removes by value
last = tasks.pop()     # removes and returns the last item
```

## Empty list, then build it

A very common pattern -- start empty and accumulate:

```python
squares = []
for n in range(1, 4):
    squares.append(n * n)
print(squares)
```

```
[1, 4, 9]
```

That "empty list plus append in a loop" shape shows up constantly in real code.
""", {
    "prompt": "Start with nums = [], append 1, 2, 3 in a loop, then print the list.",
    "starter": "nums = []\n",
    "expected": "[1, 2, 3]",
}, 'nums = []\nfor n in [1, 2, 3]:\n    nums.append(n)\nprint(nums)')

lesson("listloop", "Lists", "Looping Over Lists", """
# Looping Over Lists

The most common list operation: do something to every item.

```python
prices = [4, 10, 7]
total = 0

for price in prices:
    total = total + price

print(total)      # 21
```

Notice `for price in prices` -- no `range`, no indices. You get each item
directly. This is the idiomatic form in Python; prefer it.

## Counting a total

That `total = 0` then `total = total + price` shape is called an accumulator.
It is the standard way to total, count, or collect things in a loop.

## With an index, if you really need one

```python
for i, price in enumerate(prices):
    print(f"{i}: {price}")
```

```
0: 4
1: 10
2: 7
```

Use `enumerate()` when you need both the position and the value. Otherwise the
plain `for item in list` is cleaner.
""", {
    "prompt": "Given nums = [2, 4, 6], loop over it and print the total: 12",
    "starter": "nums = [2, 4, 6]\ntotal = 0\n",
    "expected": "12",
}, 'nums = [2, 4, 6]\ntotal = 0\nfor n in nums:\n    total = total + n\nprint(total)')

# ---------------------------------------------------------------- ch6
lesson("def", "Functions", "Functions", """
# Functions

A function is a named block of code you can run whenever you want, as many
times as you want.

```python
def greet():
    print("Hello!")

greet()
greet()
```

```
Hello!
Hello!
```

Line by line:

- `def` says "I am defining a function"
- `greet` is the name
- `()` is where inputs will go (none here)
- `:` ends the header
- the indented body is what runs when called

**Defining a function does not run it.** Nothing happens until you write
`greet()`. This confuses people constantly -- if your function "does nothing",
check you actually called it.

## Why use them?

Because the alternative is copy-pasting the same lines everywhere. Then you fix
a bug in one copy and forget the other three. Write it once, call it everywhere.
""", {
    "prompt": "Define a function named hello that prints hi, then call it once.",
    "starter": "",
    "expected": "hi",
}, 'def hello():\n    print("hi")\n\nhello()')

lesson("params", "Functions", "Parameters and return", """
# Parameters and return

## Parameters: giving the function data

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ada")
greet("Grace")
```

```
Hello, Ada!
Hello, Grace!
```

`name` is a **parameter** -- a variable that gets whatever you passed in.
`"Ada"` is the **argument** -- the actual value.

## return: giving data back

`print` shows a value on screen. `return` hands it back to the caller so it can
be used.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result * 10)    # 50
```

## print vs return -- the big one

```python
def add_print(a, b):
    print(a + b)       # shows 5, returns None

def add_return(a, b):
    return a + b       # returns 5
```

If you `print` inside a function, the caller gets `None` -- nothing usable.
Beginners lose hours to this. **Use `return` when the caller needs the value.**

A function hits `return` and stops immediately; nothing after it runs.
""", {
    "prompt": "Write a function square(n) that returns n squared, then print square(5).",
    "starter": "",
    "expected": "25",
}, 'def square(n):\n    return n * n\n\nprint(square(5))')

lesson("final", "Functions", "Putting It Together", """
# Putting It Together

Time to combine everything: a function that loops over a list and returns a
value.

```python
def total(prices):
    result = 0
    for price in prices:
        result = result + price
    return result

print(total([3, 5, 2]))   # 10
```

Read it as a sentence: *"to total a list of prices: start at 0, add each one,
hand back the result."*

## A slightly bigger example

```python
def average(numbers):
    if len(numbers) == 0:
        return 0
    return total(numbers) / len(numbers)

print(average([3, 5, 2]))    # 3.3333333333333335
print(f"{average([3, 5, 2]):.2f}")   # 3.33
```

Two things worth noticing:

1. The **guard clause**: `if len(numbers) == 0` returns early. Dividing by zero
   would crash, so we handle the empty case first. Checking odd inputs at the
   top of a function is a habit worth building.
2. Functions calling functions. `average` uses `total`. Small pieces, stacked.

## Where you go next

You now know variables, types, conditions, loops, lists and functions. That is
genuinely most of the language. Real next steps:

- Dictionaries -- key/value storage
- Reading and writing files
- `try` / `except` for handling errors
- Installing packages with `pip`
- Classes, when you meet code that needs them

Pick a small annoying task you do by hand and automate it. That teaches more
than any tutorial.
""", {
    "prompt": "Write a function biggest(nums) that returns the largest number in a list (do not use max()), then print biggest([4, 9, 2]).",
    "starter": "",
    "expected": "9",
}, 'def biggest(nums):\n    best = nums[0]\n    for n in nums:\n        if n > best:\n            best = n\n    return best\n\nprint(biggest([4, 9, 2]))')


# ---------------------------------------------------------------- emit
def build():
    out = []
    for id, chapter, title, body, exercise, solution in L:
        entry = {"id": id, "chapter": chapter, "title": title, "body": body}
        if exercise:
            entry["exercise"] = exercise
        out.append(entry)
    return {"lessons": out}


if __name__ == "__main__":
    # Self-test: run every reference solution and confirm it matches `expected`.
    import subprocess
    import sys

    failures = []
    for id, chapter, title, body, exercise, solution in L:
        if not exercise:
            continue
        proc = subprocess.run([sys.executable, "-I", "-c", solution],
                              capture_output=True, text=True, timeout=10)
        got = proc.stdout.rstrip("\n")
        want = exercise["expected"]
        if proc.returncode != 0 or got != want:
            failures.append((id, want, got, proc.stderr.strip()))

    if failures:
        for id, want, got, err in failures:
            print(f"FAIL {id}\n  want: {want!r}\n  got:  {got!r}\n  err:  {err}")
        sys.exit(1)

    path = Path(__file__).parent / "lessons.json"
    path.write_text(json.dumps(build(), indent=2, ensure_ascii=False) + "\n", "utf-8")
    n_ex = sum(1 for x in L if x[4])
    print(f"OK: {len(L)} lessons, {n_ex} exercises verified -> {path}")
