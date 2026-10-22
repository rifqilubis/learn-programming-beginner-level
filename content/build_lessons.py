#!/usr/bin/env python3
"""One-shot generator for content/lessons.json. Not shipped in the repo."""
import json
import sys
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


# ---------------------------------------------------------------- ch7: dictionaries
lesson("dicts", "Dictionaries", "Dictionaries", """
# Dictionaries

A list finds things by position -- `fruits[0]`. A dictionary finds things by
**name**. You look up a *key* to get its *value*.

```python
ages = {"Ada": 36, "Grace": 45}
print(ages["Ada"])
```

```
36
```

Curly braces, `key: value` pairs, separated by commas. This is how you store
data that has labels rather than a natural order.

## Look, change, add

```python
ages["Ada"] = 37       # key exists, so this overwrites
ages["Alan"] = 41      # key is new, so this adds
print(ages)
```

```
{'Ada': 37, 'Grace': 45, 'Alan': 41}
```

The syntax is identical whether the key exists or not, which is why it is easy
to silently overwrite something you meant to keep.

## What a missing key does

```python
print(ages["Bob"])
```

```
KeyError: 'Bob'
```

That crash is on purpose. Better to fail than to invent a value. When you are
not sure the key exists, use `.get()`:

```python
print(ages.get("Bob"))          # None
print(ages.get("Bob", 0))       # 0
```

## What keys can be

Keys are usually strings or numbers. Values can be anything -- including lists
and other dictionaries.

> If your data has names or categories, reach for a dict. If it is a sequence
> of similar things, reach for a list.
""", {
    "prompt": "Create a dict named capitals with France mapped to Paris, then print capitals[\\\"France\\\"].",
    "starter": "",
    "expected": "Paris",
}, 'capitals = {"France": "Paris"}\nprint(capitals["France"])')

lesson("dictcount", "Dictionaries", "Counting with a Dict", """
# Counting with a Dict

The classic dictionary job: count how often each thing appears.

```python
votes = ["cat", "dog", "cat", "bird", "cat"]
tally = {}

for v in votes:
    if v in tally:
        tally[v] = tally[v] + 1
    else:
        tally[v] = 1

print(tally)
```

```
{'cat': 3, 'dog': 1, 'bird': 1}
```

The `if v in tally` check is what stops the first `KeyError`. `in` works on
dictionaries -- it checks keys, not values.

## The shorter version

`dict.get(key, default)` returns the default when the key is missing, so the
branch disappears:

```python
tally = {}
for v in votes:
    tally[v] = tally.get(v, 0) + 1
```

One line that reads as: *"the count so far, or 0 if I have never seen it, plus
one."* This idiom is everywhere in real Python.

> Both versions are correct. The long one is clearer the first time you meet
> it; the short one is what you will write after a week.
""", {
    "prompt": "Given words = [\\\"a\\\", \\\"b\\\", \\\"a\\\"], build a count dict and print counts[\\\"a\\\"].",
    "starter": 'words = ["a", "b", "a"]\n',
    "expected": "2",
}, 'words = ["a", "b", "a"]\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nprint(counts["a"])')

lesson("dictloop", "Dictionaries", "Looping Over a Dict", """
# Looping Over a Dict

## Just the keys

```python
scores = {"math": 90, "art": 75}

for subject in scores:
    print(subject)
```

```
math
art
```

Looping a dictionary directly gives you the keys.

## Keys and values together

`.items()` gives you both at once:

```python
for subject, score in scores.items():
    print(f"{subject}: {score}")
```

```
math: 90
art: 75
```

That two-variable form in the `for` is called **unpacking** -- each item is a
pair, and Python splits it for you.

## Only one side

```python
print(scores.keys())     # dict_keys(['math', 'art'])
print(scores.values())   # dict_values([90, 75])
```

## Order

Dictionaries keep the order you inserted keys in, so loops come out in insertion
order. That is guaranteed in modern Python. Do not rely on it if you *need* a
particular order -- sort explicitly instead.
""", {
    "prompt": "For prices = {\\\"apple\\\": 2, \\\"pear\\\": 3}, loop with .items() and print apple: 2 then pear: 3.",
    "starter": 'prices = {"apple": 2, "pear": 3}\n',
    "expected": "apple: 2\npear: 3",
}, 'prices = {"apple": 2, "pear": 3}\nfor name, price in prices.items():\n    print(f"{name}: {price}")')

# ---------------------------------------------------------------- ch8: errors
lesson("tryexcept", "Handling Errors", "try and except", """
# try and except

An error normally stops your program. `try` / `except` lets you catch it and
decide what happens instead.

```python
try:
    number = int("abc")
except ValueError:
    print("that was not a number")
```

```
that was not a number
```

Without the `try`, this program would crash. With it, the crash became a
message you chose.

## The shape

- `try:` -- code that might fail
- `except ValueError:` -- what to do if *that specific error* happens

Perfectionists note: put **only** the risky line in the `try`. If you wrap
twenty lines, you will not know which one raised.

## Naming the error

```python
try:
    number = int("abc")
except ValueError as e:
    print(f"failed: {e}")
```

`as e` gives you the error object, so you can read its message.

## The bad version you will see everywhere

```python
try:
    risky()
except:              # catches everything, including typos in your own code
    pass             # silently does nothing
```

This hides real bugs. If a function name is misspelled, you get silence instead
of a crash telling you. Catch the **specific** error you expect, and always do
something visible with it.

> A bare `except:` is nearly always a mistake.
""", {
    "prompt": "Wrap int(\\\"abc\\\") in try/except ValueError so it prints: bad input",
    "starter": "",
    "expected": "bad input",
}, 'try:\n    int("abc")\nexcept ValueError:\n    print("bad input")')

lesson("errors2", "Handling Errors", "Common Errors", """
# Common Errors

Five errors cover almost everything you will hit as a beginner.

## TypeError -- wrong kind of thing

```python
print("age: " + 36)
```

```
TypeError: can only concatenate str (not "int") to str
```

You mixed types somewhere. Fix with `str()` or an f-string.

## ValueError -- right type, impossible value

```python
int("abc")
```

```
ValueError: invalid literal for int() with base 10: 'abc'
```

It is a string as expected, but it does not contain a number.

## NameError -- unknown name

```python
print(total)
```

```
NameError: name 'total' is not defined
```

A typo, or the variable was never created. Check spelling and that you assigned
it *before* using it.

## IndexError -- ran off the end

```python
fruits = ["apple", "banana"]
print(fruits[5])
```

```
IndexError: list index out of range
```

The list has 2 items, indices `0` and `1`. There is no `5`.

## KeyError -- missing dict key

```python
ages = {}
print(ages["Ada"])
```

```
KeyError: 'Ada'
```

Use `.get()` when the key might be absent.

## Reading them fast

The **last line** names the error type and explains it. The line above points
at the exact source line. Read those two and you usually know the fix.
""", {
    "prompt": "Given items = [\\\"x\\\"], print items[0] inside try/except IndexError. It should print x.",
    "starter": 'items = ["x"]\n',
    "expected": "x",
}, 'items = ["x"]\ntry:\n    print(items[0])\nexcept IndexError:\n    print("out of range")')

lesson("raising", "Handling Errors", "Raising Your Own", """
# Raising Your Own

Sometimes *your* code knows something is wrong before Python does. `raise` lets
you stop with your own error.

```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age

print(set_age(30))
```

```
30
```

Call it with `-1` and you get your own message instead of silence.

## Why bother?

Because the alternative is returning nonsense:

```python
def set_age(age):
    if age < 0:
        return None    # the caller may not check, and the bug travels far
```

Returning a bad value lets the mistake spread. Raising stops it at the source,
where the error message still makes sense.

## Validating at the edge

The rule of thumb: check inputs when they first enter your program, not deep
inside it. A function that validates its arguments and then trusts them is much
easier to reason about than one that re-checks everywhere.

> Think of `raise` as a smoke alarm, not a punishment. Loud and early beats
> quiet and late.
""", {
    "prompt": "Write check(n) that raises ValueError if n < 0, else returns n. Call it with 5 and print the result.",
    "starter": "",
    "expected": "5",
}, 'def check(n):\n    if n < 0:\n        raise ValueError("negative")\n    return n\n\nprint(check(5))')

# ---------------------------------------------------------------- ch9: files
lesson("reading", "Working with Files", "Reading Files", """
# Reading Files

You open a file, read it, then close it. The `with` form does the closing for
you.

```python
with open("notes.txt") as f:
    text = f.read()

print(text)
```

`with` closes the file even if something goes wrong inside the block. Use it
every time -- there is no good reason to call `.close()` by hand.

## The file is in the folder you are running from

`open("notes.txt")` looks for the file **next to your program**, not next to
wherever you happen to be browsing. This is the number-one confusion for
beginners, and it produces:

```
FileNotFoundError: [Errno 2] No such file or directory: 'notes.txt'
```

If you see that, the name is misspelled or the file is somewhere else.

## Line by line, not all at once

`.read()` pulls in the whole file. For a big file, loop instead:

```python
with open("notes.txt") as f:
    for line in f:
        print(line.strip())
```

`.strip()` removes the newline at the end of each line -- otherwise every
`print` adds a second blank line.

> In the exercise below, the file already exists in the folder. Look at the
> panel above the code box to see its contents.
""", {
    "prompt": "Read notes.txt and print its contents. The file already exists.",
    "starter": 'with open("notes.txt") as f:\n    text = f.read()\n',
    "expected": "hello",
    "files": {"notes.txt": "hello\n"},
}, 'with open("notes.txt") as f:\n    print(f.read().strip())')

lesson("writing", "Working with Files", "Writing Files", """
# Writing Files

`"w"` mode **replaces** the file. If it existed, the old contents are gone.

```python
with open("out.txt", "w") as f:
    f.write("first line\\n")
```

⚠️ `"w"` does not warn you. A typo in the filename plus `"w"` is how people
erase data they meant to append to.

## Adding instead of replacing

Use `"a"` for append:

```python
with open("out.txt", "a") as f:
    f.write("another line\\n")
```

`"a"` adds to the end and keeps what was there.

## Writing several lines

`.write()` needs newlines spelled out with `\\n`. With many lines,
`.writelines()` or a loop is clearer:

```python
with open("out.txt", "w") as f:
    for n in range(1, 4):
        f.write(f"line {n}\\n")
```

```
line 1
line 2
line 3
```

Remember that `\\n` is text you write *inside* the string. Forgetting it
produces one long line.

> Files are lost between exercises, so you can write freely. Each Submit starts
> in a fresh folder.
""", {
    "prompt": "Write one and two to out.txt (each on its own line) using w mode, then read it back and print it.",
    "starter": 'with open("out.txt", "w") as f:\n    f.write("one\\n")\n',
    "expected": "one\ntwo",
    "files": {},
}, 'with open("out.txt", "w") as f:\n    f.write("one\\n")\n    f.write("two\\n")\n\nwith open("out.txt") as f:\n    print(f.read().strip())')

lesson("filesum", "Working with Files", "Putting It Together", """
# Putting It Together: Reading and Calculating

The most useful file skill: read data, compute, print a result.

```python
with open("sales.txt") as f:
    total = 0
    for line in f:
        total = total + int(line)

print(total)
```

If `sales.txt` holds:

```
10
25
5
```

the answer is `40`.

## Watch out for the newline

Each line from a file ends in `\\n`. `int("10\\n")` actually works -- Python
ignores surrounding whitespace -- so this example is fine. But comparing raw
lines is not:

```python
if line == "10":      # never true, line is "10\\n"
```

Strip before comparing:

```python
if line.strip() == "10":
```

## Skipping blank lines

Real files have blank lines at the end. `int("")` raises `ValueError`, so guard
it:

```python
for line in f:
    line = line.strip()
    if not line:
        continue
    total = total + int(line)
```

That three-line pattern handles almost every real-world data file you will meet.

> You now have everything needed to read a spreadsheet export, total a column,
> and write the result back out.
""", {
    "prompt": "sales.txt contains 10, 25, 5 on separate lines. Read it and print the total: 40",
    "starter": "total = 0\n",
    "expected": "40",
    "files": {"sales.txt": "10\n25\n5\n"},
}, 'total = 0\nwith open("sales.txt") as f:\n    for line in f:\n        total = total + int(line)\nprint(total)')


# ---------------------------------------------------------------- ch10: strings deep
lesson("splitjoin", "Working with Strings", "Splitting and Joining", """
# Splitting and Joining

Two methods cover most text processing: `split()` turns a string into a list,
`join()` turns a list back into a string.

## split

```python
sentence = "the cat sat"
words = sentence.split()
print(words)
```

```
['the', 'cat', 'sat']
```

With no argument, `.split()` breaks on any run of whitespace -- spaces, tabs,
newlines. That makes it the right tool for messy text.

Give it a character to split on something specific:

```python
csv = "ada,grace,alan"
print(csv.split(","))
```

```
['ada', 'grace', 'alan']
```

## join

`join()` is the reverse. It is called **on the separator**, and you pass it the
list:

```python
print(" ".join(["the", "cat"]))     # the cat
print("-".join(["a", "b", "c"]))    # a-b-c
```

The order feels backwards the first time you say it out loud. Read
`" ".join(words)` as *"join these words using a space."*

## The round trip

```python
text = "one two three"
print(len(text.split()))            # 3 words
print(",".join(text.split()))       # one,two,three
```

> ⚠️ `join()` needs a list of **strings**. `",".join([1, 2])` raises
> `TypeError`. Convert first: `",".join(str(n) for n in [1, 2])`.
""", {
    "prompt": "Split the string \\\"a b c\\\" on whitespace and print how many words there are.",
    "starter": 'text = "a b c"\n',
    "expected": "3",
}, 'text = "a b c"\nprint(len(text.split()))')

lesson("strmethods", "Working with Strings", "Useful String Methods", """
# Useful String Methods

A tour of the ones you will actually use.

## strip -- remove surrounding whitespace

```python
print("  hello  ".strip())     # hello
```

The most common use in the world: cleaning a line read from a file, which
always arrives with a `\\n` on the end.

## replace

```python
print("cat sat".replace("cat", "dog"))   # dog sat
```

Replaces **every** occurrence, not just the first.

## Checking starts and ends

```python
url = "https://example.com/page"
print(url.startswith("https"))    # True
print(url.endswith(".html"))      # False
```

## Counting and finding

```python
print("banana".count("a"))      # 3
print("banana".find("na"))      # 2
```

`.find()` returns the index of the first match, or `-1` if there is none.
Careful: `-1` is falsy but also a valid-looking number, so compare explicitly
against `-1` rather than relying on truthiness.

## Changing case

```python
print("hello".upper())     # HELLO
print("HELLO".lower())     # hello
print("hello world".title())   # Hello World
```

> None of these change the original string -- they all **return a new one**.
> Strings are immutable. `word.upper()` alone does nothing; you must use the
> result.
""", {
    "prompt": "Given s = \\\"  Hello  \\\", print s with the spaces stripped.",
    "starter": 's = "  Hello  "\n',
    "expected": "Hello",
}, 's = "  Hello  "\nprint(s.strip())')

lesson("slicing", "Working with Strings", "Slicing", """
# Slicing

`[start:stop]` cuts a piece out of a string -- or a list. Start is included,
stop is **excluded**.

```python
word = "python"
print(word[0:3])    # pyt
print(word[3:])     # hon
print(word[:3])     # pyt
```

Leaving a side blank means "from the beginning" or "to the end".

## Negative indices

Counting from the end:

```python
print(word[-3:])    # hon
print(word[-1])     # n
```

`word[-3:]` is the everyday way to say "the last three characters."

## The step

A third number is the stride:

```python
print(word[::2])    # pto
print(word[::-1])   # nohtyp
```

`[::-1]` is the classic way to reverse a string. It reads as "whole string,
backwards, one at a time."

## Slicing never crashes

Out-of-range slices are clamped instead of raising:

```python
print(word[0:100])   # python
```

Compare that to `word[100]`, which **does** raise `IndexError`. Slicing is
forgiving; indexing is not.

> Slices of a list work exactly the same way -- this is not string-specific.
""", {
    "prompt": "Print the first three characters of the string python.",
    "starter": 'word = "python"\n',
    "expected": "pyt",
}, 'word = "python"\nprint(word[:3])')

# ---------------------------------------------------------------- ch11: tuples and sets
lesson("tuples", "Tuples and Sets", "Tuples", """
# Tuples

A tuple is like a list that cannot be changed. Round brackets instead of
square.

```python
point = (3, 5)
print(point[0])    # 3
```

Trying to change one fails:

```python
point[0] = 9
```

```
TypeError: 'tuple' object does not support item assignment
```

That is the point. A tuple promises it will never change, so you can pass it
around without wondering who might modify it.

## Unpacking

The useful part. A tuple can be split into named variables in one line:

```python
point = (3, 5)
x, y = point
print(x, y)    # 3 5
```

## Swapping

This works in Python because of tuples:

```python
a = 1
b = 2
a, b = b, a
print(a, b)    # 2 1
```

The right side builds a tuple `(2, 1)`, then unpacks it back. No temporary
variable needed.

## Returning several values

A function returns one thing -- but that thing can be a tuple:

```python
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([4, 9, 2])
print(low, high)    # 2 9
```

> One-item tuples need a trailing comma: `(5,)`. Without it, `(5)` is just the
> number 5 in brackets.
""", {
    "prompt": "Swap a and b using tuple unpacking, then print them: a=1, b=2 should print 2 1",
    "starter": "a = 1\nb = 2\n",
    "expected": "2 1",
}, 'a = 1\nb = 2\na, b = b, a\nprint(a, b)')

lesson("sets", "Tuples and Sets", "Sets", """
# Sets

A set is a collection with **no duplicates** and **no order**. Curly braces,
like a dict, but just values.

```python
nums = {1, 2, 2, 3, 3, 3}
print(nums)
```

```
{1, 2, 3}
```

The duplicates vanished on creation. That is the whole personality of a set.

## Removing duplicates from a list

This is the classic one-liner:

```python
words = ["a", "b", "a", "c"]
unique = set(words)
print(len(unique))        # 3
print(sorted(unique))     # ['a', 'b', 'c']
```

You need `sorted()` to print it predictably -- a set has no order, so printing
it directly can come out differently each run.

## Membership is instant

```python
print(3 in {1, 2, 3})     # True
```

Checking `in` on a set or dict is far faster than on a list, because it does
not scan. For big collections this matters.

## Adding and removing

```python
s = {1, 2}
s.add(3)
s.discard(1)
print(s)    # {2, 3}
```

`.discard()` removes if present and **never errors** -- unlike `.remove()`,
which raises `KeyError` when the item is missing.

> ⚠️ Empty set is `set()`, not `{}`. Curly braces alone make an empty *dict*.
""", {
    "prompt": "Given nums = [1, 2, 2, 3, 3, 3], print how many unique values there are.",
    "starter": "nums = [1, 2, 2, 3, 3, 3]\n",
    "expected": "3",
}, 'nums = [1, 2, 2, 3, 3, 3]\nprint(len(set(nums)))')

lesson("whichcollection", "Tuples and Sets", "Which One Do I Use?", """
# Which One Do I Use?

Four collections, four jobs.

| Type | Syntax | Ordered | Changeable | Duplicates | Use when |
|---|---|---|---|---|---|
| `list` | `[1, 2]` | yes | yes | yes | a sequence you will grow or edit |
| `tuple` | `(1, 2)` | yes | no | yes | a fixed group, like a coordinate |
| `set` | `{1, 2}` | no | yes | no | uniqueness, or fast `in` checks |
| `dict` | `{"a": 1}` | yes | yes | keys unique | labelled data, lookup by name |

## The decision in plain words

- Need to change it later? **list**
- Must never change? **tuple**
- Only care whether something is in there? **set**
- Look things up by name? **dict**

## Set operations

Sets do maths from school:

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)    # {2, 3}   both -- intersection
print(a | b)    # {1,2,3,4} either -- union
print(a - b)    # {1}      in a but not b -- difference
```

That `&` is the tidy way to answer "what do these two lists have in common?"

## A realistic mix

```python
names = ["ada", "grace", "ada"]
seen = set()
for n in names:
    seen.add(n)
print(len(seen), sorted(seen))
```

```
2 ['ada', 'grace']
```

> Start with a list every time. Convert to a set only when you need uniqueness
> or speed, and convert back with `sorted()` when you need order.
""", {
    "prompt": "Given a = [1, 2, 3] and b = [2, 3, 4], print the values they have in common, sorted.",
    "starter": "a = [1, 2, 3]\nb = [2, 3, 4]\n",
    "expected": "[2, 3]",
}, 'a = [1, 2, 3]\nb = [2, 3, 4]\nprint(sorted(set(a) & set(b)))')

# ---------------------------------------------------------------- ch12: loop patterns
lesson("nested", "Loop Patterns", "Nested Loops", """
# Nested Loops

A loop inside a loop. The inner loop runs **completely** for each step of the
outer one.

```python
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
```

```
1 1
1 2
2 1
2 2
```

Count the lines: the inner loop ran twice for `i=1`, then twice again for
`i=2`. Outer count times inner count.

## Building rows

The usual shape -- build a string, then print it once per outer pass:

```python
for i in range(2):
    row = ""
    for j in range(3):
        row = row + "*"
    print(row)
```

```
***
***
```

`print` inside the inner loop would put each star on its own line. Accumulating
into `row` and printing after the inner loop gives one line per row.

## Careful with cost

Nesting three loops over 1000 items each is a billion steps. Nested loops
multiply. If a program feels slow, check for a loop inside a loop first.

> `break` only leaves the loop it is in -- the outer loop keeps going. To leave
> both, use a flag or move the work into a function and `return`.
""", {
    "prompt": "Use two nested loops to print a 2-by-3 block of stars: two lines, three stars each.",
    "starter": "",
    "expected": "***\n***",
}, 'for i in range(2):\n    row = ""\n    for j in range(3):\n        row = row + "*"\n    print(row)')

lesson("enumzip", "Loop Patterns", "enumerate and zip", """
# enumerate and zip

Two built-ins that remove most manual index bookkeeping.

## enumerate -- item plus position

```python
for i, name in enumerate(["ada", "grace"]):
    print(i, name)
```

```
0 ada
1 grace
```

Start counting at 1 with `start=1`:

```python
for i, name in enumerate(["ada", "grace"], start=1):
    print(f"{i}. {name}")
```

```
1. ada
2. grace
```

## zip -- walk two lists together

```python
names = ["ada", "grace"]
ages = [36, 45]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

```
ada is 36
grace is 45
```

`zip` pairs the first of each, the second of each, and so on.

> ⚠️ `zip` stops at the **shortest** list, silently. If the lists should be the
> same length, check `len()` first -- a truncated loop is easy to miss.
""", {
    "prompt": "Zip names = [Ada, Grace] with ages = [36, 45] and print each as: Ada is 36",
    "starter": 'names = ["Ada", "Grace"]\nages = [36, 45]\n',
    "expected": "Ada is 36\nGrace is 45",
}, 'names = ["Ada", "Grace"]\nages = [36, 45]\nfor name, age in zip(names, ages):\n    print(f"{name} is {age}")')

lesson("comprehensions", "Loop Patterns", "List Comprehensions", """
# List Comprehensions

A loop that builds a list, written in one line. Once it clicks, you will use it
constantly.

Compare:

```python
squares = []
for n in range(1, 4):
    squares.append(n * n)
```

with:

```python
squares = [n * n for n in range(1, 4)]
```

Both produce `[1, 4, 9]`. The second says *"a list of `n*n`, for each `n`."*

## The pattern

```
[ expression  for item in sequence ]
```

Read it right to left if that helps: for each item, produce the expression.

## With a filter

Add `if` at the end:

```python
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
print(evens)
```

```
[2, 4, 6]
```

## With a transform and a filter

```python
print([n * 10 for n in nums if n > 3])
```

```
[40, 50, 60]
```

## Dicts too

```python
print({n: n * n for n in range(1, 4)})
```

```
{1: 1, 2: 4, 3: 9}
```

> Keep it to one `for` and at most one `if`. The moment a comprehension needs
> squinting, a plain loop is better code. Shorter is not the same as clearer.
""", {
    "prompt": "Use a list comprehension to build the squares of 1, 2, 3 and print the list.",
    "starter": "",
    "expected": "[1, 4, 9]",
}, 'print([n * n for n in range(1, 4)])')


# ---------------------------------------------------------------- ch12: none and scope
lesson("none", "None and Scope", "None", """
# None

`None` is Python's way of saying *no value here*. It is not `0`, not `""`, and
not `False` -- it is the absence of a value.

You have already met it. This function prints but never returns:

```python
def greet():
    print("hello")

result = greet()
print(result)
```

```
hello
None
```

`greet()` returns `None` because it has no `return`. That is the single most
common source of `None` in your programs: **a function that forgot to return**.

## Checking for None

Use `is`, not `==`:

```python
if result is None:
    print("nothing came back")
```

`is` asks "is this the very same object?" and there is exactly one `None`, so
it is both correct and the idiomatic spelling. Keep `==` for comparing values
like numbers and text.

## None is falsy

```python
if not result:
    print("empty")
```

This catches `None`, but it also catches `0`, `""` and `[]`. When you
specifically mean "no value", say `is None` so the reader knows you meant it.

> A function that returns `None` by accident usually means a missing `return`.
> If you see `None` printed where you expected a number, look for that first.
""", {
    "prompt": "The function below prints but does not return. Fix it so find_min prints 1.",
    "starter": 'def find_min(numbers):\n    print(min(numbers))\n\nprint(find_min([3, 8, 1]))\n',
    "expected": "1",
}, 'def find_min(numbers):\n    return min(numbers)\n\nprint(find_min([3, 8, 1]))')

lesson("scope", "None and Scope", "Local and Global Scope", """
# Local and Global Scope

A variable created **inside** a function only exists inside that function.

```python
def make_greeting():
    message = "hi"
    return message

make_greeting()
print(message)
```

```
NameError: name 'message' is not defined
```

`message` is *local* to `make_greeting`. When the function ends, it is gone.
This is a feature, not a limitation: two functions can both use the name
`total` without interfering.

## Reading a global is fine

A function can *read* a variable defined outside it:

```python
rate = 0.2

def with_tax(price):
    return price + price * rate
```

`with_tax` can see `rate` because nothing shadows it locally.

## Assigning creates a new local

This is the trap:

```python
count = 0

def bump():
    count = count + 1     # UnboundLocalError
```

Because `bump` *assigns* to `count`, Python treats `count` as local for the
whole function -- so `count + 1` reads a local that does not exist yet.
The error is `UnboundLocalError`, and it confuses everyone the first time.

## The fix: pass it in, return it out

```python
def bump(count):
    return count + 1

count = bump(count)
```

Reaching for `global` "fixes" this too, but it makes data flow invisible. Pass
values in as parameters and return the new value instead. It is clearer, and it
is easier to test.

> Rule of thumb: a function should depend on its parameters and its return
> value, not on variables that happen to be lying around outside it.
""", {
    "prompt": "bump() raises UnboundLocalError. Fix it by passing count in and returning the new value, so the output is 1.",
    "starter": 'count = 0\n\ndef bump():\n    count = count + 1\n\nbump()\nprint(count)\n',
    "expected": "1",
}, 'count = 0\n\ndef bump(n):\n    return n + 1\n\ncount = bump(count)\nprint(count)')

# ---------------------------------------------------------------- ch13: classes
lesson("classes", "Classes", "Classes and Objects", """
# Classes and Objects

A class bundles **data** and the **functions that work on it** into one named
thing. You have used classes already: every string is a `str` object, which is
why `"hi".upper()` works.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex", 3)
print(rex.name)
print(rex.age)
```

```
Rex
3
```

## Reading the pieces

- `class Dog:` -- defines a new type, capitalised by convention.
- `__init__` -- runs automatically when you create a `Dog(...)`. The double
  underscores mean "Python calls this for you".
- `self` -- the particular dog being created. `self.name = name` stores the
  value on that object.
- `Dog("Rex", 3)` -- creates one object, called an *instance*.

You never write `self` when calling. Python fills it in:

```python
rex = Dog("Rex", 3)   # self is rex, name is "Rex", age is 3
```

## Why bother?

Without a class you would carry `name` and `age` around as loose variables and
pass both to every function. With one, they travel together:

```python
dogs = [Dog("Rex", 3), Dog("Pip", 1)]
for dog in dogs:
    print(dog.name)
```

That list holds whole dogs, not parallel lists of names and ages that can drift
out of sync.

> `__init__` is not "the constructor" in the C++ sense and it does not return
> anything. It fills in a new object that already exists.
""", {
    "prompt": "Create a class Book whose __init__ stores title and pages, then print the title of Book(\"Dune\", 412).",
    "starter": 'class Book:\n    def __init__(self, title, pages):\n        pass\n\nb = Book("Dune", 412)\nprint(b.title)\n',
    "expected": "Dune",
}, 'class Book:\n    def __init__(self, title, pages):\n        self.title = title\n        self.pages = pages\n\nb = Book("Dune", 412)\nprint(b.title)')

lesson("methods", "Classes", "Methods", """
# Methods

A function defined inside a class is called a **method**. It always takes
`self` first, which is how it reaches the object's own data.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count = self.count + 1

c = Counter()
c.add()
c.add()
print(c.count)
```

```
2
```

`self.count` means "the count belonging to *this* counter". Because each object
has its own, two counters do not share a number.

## Methods that take arguments

```python
class Counter:
    def __init__(self):
        self.count = 0

    def add(self, amount):
        self.count = self.count + amount

c = Counter()
c.add(5)
print(c.count)     # 5
```

Note the call: `c.add(5)`, not `c.add(c, 5)`. Python passes `c` as `self` for
you.

## Forgetting self

The most common beginner error:

```python
class Counter:
    def add():
        return 1

c = Counter()
c.add()
```

```
TypeError: Counter.add() takes 0 positional arguments but 1 was given
```

The "1 was given" is the object itself, arriving as `self`. When you see that
error in a class, add `self` as the first parameter.

## __str__ makes printing nicer

```python
class Counter:
    def __init__(self):
        self.count = 0

    def __str__(self):
        return f"Counter({self.count})"

print(Counter())
```

```
Counter(0)
```

Without `__str__`, printing an object gives `<__main__.Counter object at
0x...>`, which tells you nothing.

> Pick the method names your objects suggest: `add`, `total`, `describe`. If
> you find yourself writing `do_stuff(self, x, y)`, the class may be doing too
> much.
""", {
    "prompt": "Give Bank a deposit(amount) method so deposit(50) then print(balance) shows 50.",
    "starter": 'class Bank:\n    def __init__(self):\n        self.balance = 0\n\nb = Bank()\nb.deposit(50)\nprint(b.balance)\n',
    "expected": "50",
}, 'class Bank:\n    def __init__(self):\n        self.balance = 0\n\n    def deposit(self, amount):\n        self.balance = self.balance + amount\n\nb = Bank()\nb.deposit(50)\nprint(b.balance)')

lesson("inheritance", "Classes", "Inheritance", """
# Inheritance

A class can build on another, keeping its data and methods and adding its own.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

a = Animal("Generic")
d = Dog("Rex")
print(a.speak())
print(d.speak())
```

```
...
Woof
```

`class Dog(Animal)` means "Dog is an Animal, plus changes". `Dog` inherits
`__init__`, so `Dog("Rex")` sets `name` without you rewriting it. It overrides
`speak`.

## Calling the parent's version

Sometimes you want the parent's work *and* your own:

```python
class Puppy(Dog):
    def __init__(self, name, weeks):
        super().__init__(name)      # let Dog set up name
        self.weeks = weeks
```

`super()` gives you the parent class. Calling `super().__init__(name)` runs the
parent's setup, then you add `weeks`. Forgetting this is a classic bug: the
object exists but `name` was never set.

## When not to inherit

Inheritance means **is-a**. A `Dog` *is an* `Animal`. That is the test.

It is not for sharing code between unrelated things. A `Car` and a `User` both
having an `id` does not make one a subclass of the other. When the relationship
is "has-a" or "can-do", plain attributes or a shared function are clearer.

> Prefer simple composition until inheritance is obviously right: an object
> holding another object is easier to follow than a five-level class tree.
""", {
    "prompt": "Make Cat a subclass of Animal that overrides speak() to return \"Meow\", so the output is Meow.",
    "starter": 'class Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        return "..."\n\nclass Cat:\n    pass\n\nprint(Cat("Tom").speak())\n',
    "expected": "Meow",
}, 'class Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        return "..."\n\nclass Cat(Animal):\n    def speak(self):\n        return "Meow"\n\nprint(Cat("Tom").speak())')

# ---------------------------------------------------------------- ch14: modules and stdlib
lesson("imports", "Modules and the Standard Library", "Importing Modules", """
# Importing Modules

A **module** is a file of Python code you can reuse. `import` loads one.

```python
import math

print(math.sqrt(16))
print(math.pi)
```

```
4.0
3.141592653589793
```

The module name is a prefix, so you always see where `sqrt` came from. That is
worth the typing.

## Three forms

```python
import math                 # math.sqrt(16)
from math import sqrt       # sqrt(16)
from math import sqrt as s  # s(16)
```

Prefer plain `import math`. When you later read `sqrt(16)` alone you may not
remember which library it came from, and `math.sqrt` is unambiguous.

## A local file can shadow a library

Python looks in your own folder **before** the standard library. So if you
create a file called `random.py` next to your program, then:

```python
import random        # imports YOUR file, not the library
```

This produces confusing errors like `AttributeError: module 'random' has no
attribute 'choice'`. The rule: **never name a file after a module you also
import** -- `random.py`, `math.py`, `json.py`, `csv.py`, `string.py`. If a
library suddenly seems to be missing its functions, check for a name clash
first.

The important point: **the names you import become ordinary variables** in your
file, so two modules offering the same name can clash.

## Importing your own file

Any `.py` file next to your program is importable by its filename, without the
`.py`:

```
project/
  main.py
  helpers.py
```

```python
# main.py
import helpers

print(helpers.double(4))
```

```python
# helpers.py
def double(n):
    return n * 2
```

Nothing special is needed. Both files just sit in the same folder. Modules are
only found in the folder you run from and Python's own library -- which is why
a misspelled filename raises `ModuleNotFoundError`.

> An import runs the whole file once, top to bottom, the first time it is
> imported. Put code that *does* things behind a `if __name__ == "__main__":`
> guard (a later lesson) so importing a file does not start the program.
""", {
    "prompt": "Use math to print the square root of 81. The expected output is 9.0.",
    "starter": "",
    "expected": "9.0",
}, 'import math\n\nprint(math.sqrt(81))')

lesson("stdlib", "Modules and the Standard Library", "The Standard Library", """
# The Standard Library

Python ships with a large library. You have already met `math`. A few more you
will use constantly:

| Module | For | Example |
| --- | --- | --- |
| `math` | numbers beyond arithmetic | `math.sqrt(9)`, `math.floor(2.7)` |
| `random` | picking at random | `random.choice(["a", "b"])` |
| `datetime` | dates and times | `datetime.date.today()` |
| `json` | saving data as text | `json.dumps({"a": 1})` |
| `csv` | spreadsheets | `csv.reader(f)` |
| `pathlib` | file paths | `Path("a") / "b.txt"` |

## random must be seeded to be predictable

`random` gives different answers on every run, which is the point. For a
lesson, or a test, you want the same answer every time:

```python
import random

random.seed(42)
print(random.randint(1, 6))
print(random.choice(["red", "green", "blue"]))
```

Seeding sets the starting point, so the same seed produces the same sequence.
Tests use this to avoid flaky results.

## math.floor vs int

```python
import math

print(math.floor(-2.5))   # -3  (down)
print(int(-2.5))          # -2  (towards zero)
```

They disagree on negatives. `floor` always goes down; `int` always goes towards
zero. Use `int` for "chop off the decimals" and `floor` for real rounding down.

## datetime

```python
import datetime

today = datetime.date(2024, 1, 31)
print(today.year)
print(today.month)
```

The standard library is the first place to look before writing your own
function. Somebody has usually already written it, tested it, and documented the
edge cases.

> `import this` in a Python shell prints the Zen of Python. It is a good read
> once a year.
""", {
    "prompt": "Seed random with 42, import choice from random under another name, and print pick([\"red\", \"green\", \"blue\"]). The output is blue.",
    "starter": "import random\n",
    "expected": "blue",
}, 'import random\nfrom random import choice as pick\n\nrandom.seed(42)\nprint(pick(["red", "green", "blue"]))')

lesson("ownmodule", "Modules and the Standard Library", "Writing Your Own Module", """
# Writing Your Own Module

Big programs are not one long file. You split helpers into a module and import
them.

The exercise below already has `greeting.py` next to your program:

```python
# greeting.py
def hello(name):
    return f"Hello, {name}!"
```

Use it from `main.py`:

```python
# main.py
import greeting

print(greeting.hello("Ana"))
```

```
Hello, Ana!
```

That is the whole idea. The file name *is* the module name.

## Import functions directly

```python
from greeting import hello

print(hello("Ana"))
```

`from x import y` copies `y` into your file. Handy for one function; confusing
once a file imports from six modules.

## What the import executes

Importing runs the module top to bottom, once. If `greeting.py` had

```python
print("greeting.py loaded")
```

at the top level, that line would run during `import greeting`. This is why
modules should mostly define functions and avoid doing work on import.

The guard fixes it:

```python
if __name__ == "__main__":
    print("only runs when executed directly")
```

Inside a module, `__name__` is the module's name (`"greeting"`). In the file you
run directly, it is `"__main__"`. So that block runs only for the main program,
never on import.

> Split a file when it gets long enough to need scrolling, or when a group of
> functions clearly belongs together. Not before.
""", {
    "prompt": "greeting.py already exists. Import it and print greeting.hello(\"Ana\"), which should give: Hello, Ana!",
    "starter": "",
    "expected": "Hello, Ana!",
    "files": {"greeting.py": 'def hello(name):\n    return f"Hello, {name}!"\n'},
}, 'import greeting\n\nprint(greeting.hello("Ana"))')

# ---------------------------------------------------------------- ch15: sorting and lambdas
lesson("sorting", "Sorting and Lambdas", "sort and sorted", """
# sort and sorted

Two ways to put a list in order. They are not the same.

```python
nums = [3, 1, 2]

nums.sort()          # changes nums in place
print(nums)          # [1, 2, 3]

letters = ["b", "c", "a"]
ordered = sorted(letters)   # returns a NEW list
print(ordered)       # ['a', 'b', 'c']
print(letters)       # ['b', 'c', 'a']  unchanged
```

- `.sort()` -- a method, edits the list, returns `None`.
- `sorted()` -- a function, leaves the original alone, returns a new list.

`.sort()` returning `None` catches everyone once:

```python
nums = [3, 1, 2]
nums = nums.sort()
print(nums)      # None
```

If you print `None` after sorting, that is why. Either call `.sort()` without
assigning, or use `sorted()`.

## Backwards

```python
print(sorted([3, 1, 2], reverse=True))
```

```
[3, 2, 1]
```

## Strings sort by character code

```python
print(sorted(["banana", "Apple", "cherry"]))
```

```
['Apple', 'banana', 'cherry']
```

Capital letters come before lowercase, so `"Apple"` leads. For a
case-insensitive sort you need a `key` -- the next lesson.

> `sorted()` works on any sequence, including the characters of a string and the
> keys of a dict. `.sort()` only exists on lists.
""", {
    "prompt": "Sort the list in place so it prints in ascending order.",
    "starter": "nums = [5, 2, 9, 1]\n",
    "expected": "[1, 2, 5, 9]",
}, 'nums = [5, 2, 9, 1]\nnums.sort()\nprint(nums)')

lesson("keyfunctions", "Sorting and Lambdas", "Sorting with key", """
# Sorting with key

Real data is rarely a plain list of numbers. `key` tells Python *what to sort
by*.

```python
words = ["banana", "Apple", "cherry"]
print(sorted(words, key=str.lower))
```

```
['Apple', 'banana', 'cherry']
```

`key=str.lower` means: for each word, compare its lowercase form. The original
words are untouched -- `key` only decides the order.

## Sorting records

```python
people = [
    {"name": "Ana", "age": 31},
    {"name": "Bo", "age": 25},
]

by_age = sorted(people, key=lambda p: p["age"])
print(by_age[0]["name"])
```

```
Bo
```

`lambda p: p["age"]` is a tiny unnamed function: "given `p`, return `p["age"]`".
A `lambda` is just a function you did not bother naming.

## The same thing with a named function

```python
def age_of(person):
    return person["age"]

by_age = sorted(people, key=age_of)
```

This is often clearer, and it can be given a docstring or tested. Reach for
`lambda` when the expression is short enough to read inline.

## Sorting on several fields

Return a tuple and Python compares it left to right:

```python
sorted(people, key=lambda p: (p["age"], p["name"]))
```

That sorts by age, and breaks ties by name.

> If a `key` needs more than one short expression, write a named function. A
> three-line `lambda` is a sign you wanted `def`.
""", {
    "prompt": "Sort the words case-insensitively so the output is ['Apple', 'banana', 'cherry'].",
    "starter": 'words = ["banana", "Apple", "cherry"]\n',
    "expected": "['Apple', 'banana', 'cherry']",
}, 'words = ["banana", "Apple", "cherry"]\nprint(sorted(words, key=str.lower))')

lesson("lambdas", "Sorting and Lambdas", "The Built-in Helpers", """
# The Built-in Helpers

Python has small functions that replace the loops you would otherwise write by
hand. All of these take a sequence:

| Function | Answers |
| --- | --- |
| `sum(xs)` | total |
| `min(xs)` / `max(xs)` | smallest / largest |
| `len(xs)` | how many |
| `any(xs)` | is at least one true? |
| `all(xs)` | are they all true? |
| `sorted(xs)` | a sorted copy |

```python
nums = [4, 8, 1]

print(sum(nums))     # 13
print(max(nums))     # 8
print(min(nums))     # 1
print(len(nums))     # 3
```

## any and all

```python
scores = [80, 45, 90]

print(any(s < 50 for s in scores))   # True
print(all(s >= 50 for s in scores))  # False
```

`any(... for ...)` is a generator expression -- it feeds values to `any` one at
a time, without building a list. Read it as "is there any score under 50?".

## max with a key

`max` accepts `key`, just like `sorted`:

```python
people = [{"name": "Ana", "age": 31}, {"name": "Bo", "age": 25}]
oldest = max(people, key=lambda p: p["age"])
print(oldest["name"])
```

```
Ana
```

## These do not replace every loop

A `for` loop is still the right tool when you must *do* something per item --
print, write a file, call an API. `sum` and friends are for *computing one
answer* from a sequence.

> Writing `total = 0` then `for n in nums: total += n` is correct but noisy.
> `sum(nums)` says what you meant in four characters.
""", {
    "prompt": "Using the helper functions, print the largest score and the total on separate lines (output: 90 then 215).",
    "starter": 'scores = [80, 45, 90]\n',
    "expected": "90\n215",
}, 'scores = [80, 45, 90]\nprint(max(scores))\nprint(sum(scores))')

# ---------------------------------------------------------------- ch16: data formats
lesson("json", "Data Formats", "JSON", """
# JSON

JSON is text that represents data. It looks like Python literals, and every
language can read it -- which is why APIs and config files use it.

```python
import json

data = {"name": "Ana", "age": 31, "tags": ["admin", "editor"]}
text = json.dumps(data)
print(text)
```

```
{"name": "Ana", "age": 31, "tags": ["admin", "editor"]}
```

`dumps` means **d**ump **s**tring: Python value -> JSON text.

## Reading it back

```python
text = '{"name": "Ana", "age": 31}'
data = json.loads(text)
print(data["name"])
```

```
Ana
```

`loads` means **load** **s**tring: JSON text -> Python value. The `s` is the
only difference between the two names, and mixing them up is the usual mistake.

## The mappings

| JSON | Python |
| --- | --- |
| object `{}` | `dict` |
| array `[]` | `list` |
| string | `str` |
| number | `int` / `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

Note the last two: Python writes `True` and `None`, JSON uses `true` and `null`.
`json.dumps` translates for you. Typing JSON by hand in Python syntax is the
common error.

## Pretty printing

```python
print(json.dumps(data, indent=2))
```

Adds newlines and spaces so a human can read it. Never ship indented JSON to a
size-critical place, but do use it when debugging.

## Bad JSON raises an error

```python
json.loads("{bad}")
```

```
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
```

JSON requires **double** quotes. Single quotes are not valid, even though
Python accepts them.

> `dumps` and `loads` work on strings. The file versions are `dump` and `load`
> -- no `s`. Same idea, different source.
""", {
    "prompt": "Turn the dict into JSON text and print it. The output must be: {\"a\": 1, \"b\": 2}",
    "starter": 'import json\n\ndata = {"a": 1, "b": 2}\n',
    "expected": '{"a": 1, "b": 2}',
}, 'import json\n\ndata = {"a": 1, "b": 2}\nprint(json.dumps(data))')

lesson("jsonfiles", "Data Formats", "Saving Data with JSON Files", """
# Saving Data with JSON Files

`json.dump` writes straight to a file; `json.load` reads one back. No `s`.

```python
import json

data = {"visits": 3, "name": "Ana"}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json") as f:
    loaded = json.load(f)

print(loaded["name"])
```

```
Ana
```

Notice the pattern: `open` plus `json.dump`, not `json.dumps` then `f.write`.
Both work, but the direct form is shorter and avoids one mistake.

## JSON has no tuples or sets

```python
import json

print(json.dumps((1, 2)))   # [1, 2]
```

Tuples come back as lists. Sets are not JSON at all -- `json.dumps({1, 2})`
raises `TypeError`. Convert first with `sorted(the_set)` or `list(the_set)` if
order does not matter.

## Numbers stay numbers

```python
import json

data = json.loads('{"n": 5}')
print(data["n"] + 1)      # 6
```

JSON numbers become real `int`/`float`, so arithmetic works immediately. This is
why JSON is a better fit than plain text for structured data.

## The round trip

Save, load, and confirm you got the same thing:

```python
original = {"a": [1, 2], "b": None}
again = json.loads(json.dumps(original))
print(again == original)    # True
```

Being able to say that confidently is how you check a save/load bug.

> If a file is empty, `json.load` raises `JSONDecodeError`. Check
> `f.read()` first, or create the file with default contents when it is missing.
""", {
    "prompt": "Write data.json containing {\"hits\": 7}, read it back, and print the value under \"hits\".",
    "starter": "import json\n\ndata = {'hits': 7}\n",
    "expected": "7",
}, 'import json\n\ndata = {"hits": 7}\n\nwith open("data.json", "w") as f:\n    json.dump(data, f)\n\nwith open("data.json") as f:\n    loaded = json.load(f)\n\nprint(loaded["hits"])')

lesson("csvfiles", "Data Formats", "CSV Files", """
# CSV Files

CSV is a spreadsheet as plain text: values separated by commas, one row per
line.

```
name,score
Ana,90
Bo,75
```

The first row is usually the header.

## Reading

```python
import csv

with open("scores.csv", newline="") as f:
    rows = list(csv.reader(f))

for row in rows:
    print(row)
```

```
['name', 'score']
['Ana', '90']
['Bo', '75']
```

Two things to notice:

- `csv.reader` gives **lists of strings**. `"90"`, not `90`.
- Use `newline=""` when opening. Without it, Windows line endings can produce
  blank rows. It is harmless on Linux and correct everywhere.

## Skipping the header

```python
with open("scores.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)            # throw away the header row
    for row in reader:
        print(row[0], row[1])
```

`next(reader)` pulls one row and discards it. That is the whole trick.

## DictReader is friendlier

```python
with open("scores.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["score"])
```

`DictReader` uses the header as keys, so you write `row["name"]` instead of
`row[0]`. It keeps working when somebody inserts a column in the middle.

## Writing

```python
import csv

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Ana", 90])
```

`writerow` takes one list per row. Pass numbers, not strings -- it converts them.

> Values containing commas are quoted automatically by `csv`. Do not split on
> `","` yourself; that breaks the moment a field contains a comma.
""", {
    "prompt": "scores.csv already exists. Skip the header and print each name, one per line (Ana then Bo).",
    "starter": 'import csv\n\nwith open("scores.csv", newline="") as f:\n    rows = list(csv.reader(f))\n',
    "expected": "Ana\nBo",
    "files": {"scores.csv": "name,score\nAna,90\nBo,75\n"},
}, 'import csv\n\nwith open("scores.csv", newline="") as f:\n    reader = csv.reader(f)\n    next(reader)\n    for row in reader:\n        print(row[0])')

# ---------------------------------------------------------------- ch17: recursion and algorithms
lesson("recursion", "Recursion and Algorithms", "Recursion", """
# Recursion

A recursive function calls **itself** on a smaller version of the problem. Every
recursive function needs two parts:

1. a **base case** -- when to stop
2. a **recursive case** -- call itself with something smaller

```python
def countdown(n):
    if n == 0:          # base case
        print("go")
        return
    print(n)
    countdown(n - 1)    # recursive case, smaller

countdown(3)
```

```
3
2
1
go
```

## Why it works

Each call gets a smaller `n`, so it must eventually reach `0`. Remove the base
case and it calls forever:

```
RecursionError: maximum recursion depth exceeded
```

That error means "you forgot the base case", or the value never actually gets
smaller.

## A classic: factorial

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

```
120
```

Read it as: `5 * 4 * 3 * 2 * 1`. The function trusts that `factorial(n - 1)`
already works, and builds on that.

## Any loop can do this

```python
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
```

Faster, and uses no extra memory. In Python, recursion is mostly a teaching
tool -- the loop is usually the better choice. Recursion wins when the data
itself is nested: a folder containing folders, or a tree.

> If you can picture the problem shrinking toward a stopping point, recursion
> will fit. If you cannot, use a loop.
""", {
    "prompt": "Write a recursive count_down(n) that prints n down to 1 on separate lines. Call count_down(3).",
    "starter": "def count_down(n):\n    # your code here\n    pass\n\ncount_down(3)\n",
    "expected": "3\n2\n1",
}, 'def count_down(n):\n    if n == 0:\n        return\n    print(n)\n    count_down(n - 1)\n\ncount_down(3)')

lesson("searching", "Recursion and Algorithms", "Searching", """
# Searching

Finding something in a collection is the most common real task. Two approaches,
and the choice matters once the data is big.

## Linear search: look at everything

```python
def find(names, target):
    for name in names:
        if name == target:
            return name
    return None

print(find(["Ana", "Bo", "Cy"], "Bo"))
```

```
Bo
```

One comparison per item. For 1,000 items, up to 1,000 checks. Simple, and
correct on unsorted data.

## Returning None when absent

That `return None` at the end is important. Without it the function returns
`None` anyway, but writing it makes the intent obvious to the next reader.

## Python already has this

```python
if "Bo" in names:
    print("found")

names.index("Bo")   # position, raises ValueError if missing
```

Use `in` for "does it exist?" and `.index()` when you need the position. Reach
for a hand-written loop only when the *match is complicated* -- for example,
"the first person over 30".

## Binary search: only on sorted data

If a list is sorted, halve it each time:

```python
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

For 1,000 sorted items that is about 10 comparisons instead of 1,000. The price
is that the data must be sorted first, and sorting costs more than one search.

> Rule of thumb: one lookup -- loop. Thousands of lookups on fixed data -- sort
> once, then use binary search or a dict keyed by the thing you search for.
""", {
    "prompt": "Finish find(): return the first name longer than 3 letters, or None. Print it, so the output is Anabel.",
    "starter": 'def find(names):\n    for name in names:\n        pass\n    return None\n\nprint(find(["Bo", "Anabel", "Cy"]))\n',
    "expected": "Anabel",
}, 'def find(names):\n    for name in names:\n        if len(name) > 3:\n            return name\n    return None\n\nprint(find(["Bo", "Anabel", "Cy"]))')

lesson("algorithms", "Recursion and Algorithms", "Common Algorithms", """
# Common Algorithms

A handful of small patterns solve most beginner problems. Learn to recognise
them.

## Counting

```python
text = "hello world"
count = 0
for ch in text:
    if ch == "l":
        count = count + 1
print(count)
```

Or, shorter, `text.count("l")`.

## Total and average

```python
nums = [4, 8, 2]

total = sum(nums)
average = total / len(nums)
print(total, average)
```

Guard the empty case: `sum([]) / len([])` raises `ZeroDivisionError` because
`len([])` is `0`.

## Finding the biggest

```python
biggest = nums[0]
for n in nums[1:]:
    if n > biggest:
        biggest = n
```

This is `max(nums)`. Writing it once by hand teaches the pattern; after that,
use `max`.

## De-duplicating while keeping order

A set removes duplicates but loses order:

```python
names = ["Ana", "Bo", "Ana", "Cy"]
print(list(set(names)))       # order not guaranteed
```

To keep first-seen order:

```python
seen = set()
unique = []
for name in names:
    if name not in seen:
        seen.add(name)
        unique.append(name)
print(unique)
```

```
['Ana', 'Bo', 'Cy']
```

That `seen` set plus `unique` list pattern appears in real code constantly --
`if name not in seen` is O(1) on a set, so it stays fast on big data.

## FizzBuzz

The classic, because it combines the pieces: loop, modulus, conditions.

```python
for n in range(1, 6):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
```

Check the **most specific** condition first. Testing `% 3` before `% 15` would
print `Fizz` for 15.

> When a problem looks new, ask which of these it is: count, total, find,
> filter, dedupe, or combine. It nearly always is one of them.
""", {
    "prompt": "Print Fizz for multiples of 3 and Buzz for multiples of 5, from 1 to 5, one per line. So: 1, 2, Fizz, 4, Buzz.",
    "starter": "for n in range(1, 6):\n    pass\n",
    "expected": "1\n2\nFizz\n4\nBuzz",
}, 'for n in range(1, 6):\n    if n % 3 == 0:\n        print("Fizz")\n    elif n % 5 == 0:\n        print("Buzz")\n    else:\n        print(n)')

# ---------------------------------------------------------------- ch18: testing and debugging
lesson("asserts", "Testing and Debugging", "Checking with assert", """
# Checking with assert

`assert` states something you believe is true. If it is not, Python stops
immediately and tells you.

```python
def double(n):
    return n * 2

assert double(2) == 4
assert double(0) == 0

print("all good")
```

```
all good
```

No output from the asserts means they all passed.

## When one fails

```python
assert double(3) == 7
```

```
AssertionError
```

The program stops at that line. Any lines after it never run -- which is the
point: a broken assumption should not be allowed to quietly poison everything
downstream.

## Add a message

```python
assert double(3) == 6, "double(3) should be 6"
```

Now the failure says what you meant, not just that something is wrong. Always
include the message when the expression is not obvious.

## Assertions check *code*, not user input

`assert` is for finding bugs while you develop. It is **not** for validating
data a user typed:

```python
def withdraw(amount):
    assert amount > 0, "amount must be positive"    # wrong tool
```

Anyone can run Python with assertions switched off (`python3 -O`), so this check
would silently vanish in production. For real validation, raise:

```python
def withdraw(amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
```

Use `assert` on things that would mean *your code is wrong*. Use `raise` on
things that mean *the caller is wrong*.

## A tiny test suite

```python
assert double(2) == 4
assert double(-1) == -2
assert double(0) == 0
print("tests passed")
```

That is a real, useful test suite. Professionals use `pytest` for the reporting,
but the idea is identical: state what should be true and let the machine check
it.

> Write the assertion first, watch it fail, then write the code that makes it
> pass. You will never wonder whether your test does anything.
""", {
    "prompt": "Assert that add(2, 3) equals 5 and that add(-1, 1) equals 0, then print all good.",
    "starter": "def add(a, b):\n    return a + b\n\n\n",
    "expected": "all good",
}, 'def add(a, b):\n    return a + b\n\nassert add(2, 3) == 5\nassert add(-1, 1) == 0\nprint("all good")')

lesson("tracebacks", "Testing and Debugging", "Reading Tracebacks", """
# Reading Tracebacks

A traceback looks scary and is actually a map. Read it **from the bottom up**.

```
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    print(total / count)
          ~~~~~~^~~~~~~
ZeroDivisionError: division by zero
```

Four pieces, in order of usefulness:

1. **Last line** -- the error type and message: `ZeroDivisionError: division by
   zero`. That is the *what*.
2. **The line above it** -- your source line, with `^` pointing at the exact
   expression that broke.
3. **The `File` lines** -- *where*. The last one is your code; earlier ones are
   library internals you usually do not care about.
4. **`Traceback (most recent call last)`** -- so the final frame is the failure
   site.

## The common errors and what they mean

| Error | Usually means |
| --- | --- |
| `NameError` | typo, or variable not defined yet |
| `TypeError` | wrong kind of value, e.g. `"a" + 1` |
| `ValueError` | right kind, wrong content, e.g. `int("abc")` |
| `IndexError` | list index past the end |
| `KeyError` | dict key not present |
| `AttributeError` | `.method()` does not exist on that type |
| `ZeroDivisionError` | dividing by zero |

## The frame that matters

Long tracebacks have many frames. Only **one** of them is your file. Find the
`main.py` line and start there.

## A stack of calls

```python
def a():
    return b()

def b():
    return 1 / 0

a()
```

The traceback lists `a` calling `b` calling the bad line. The bottom frame is
where it broke; the frames above are how it got there. Both matter when a helper
is called from the wrong place.

## What to do with it

1. Read the last line. Identify the error type.
2. Find your line and look at the values on it.
3. `print()` the suspicious variable just before the failing line.

That third step solves most bugs. The traceback tells you *where*; printing
tells you *what the value actually was*, which is usually not what you assumed.

> Never paste a traceback away and rewrite the function from scratch. The answer
> is already in the message -- read the bottom line first.
""", {
    "prompt": "This code raises an IndexError. Fix it so it prints the last item, banana.",
    "starter": 'fruits = ["apple", "banana"]\nprint(fruits[2])\n',
    "expected": "banana",
}, 'fruits = ["apple", "banana"]\nprint(fruits[-1])')

lesson("debugging", "Testing and Debugging", "Debugging a Bug", """
# Debugging a Bug

Bugs are not mysterious. There is a gap between what you think the code does and
what it does. Debugging is closing that gap.

## Step 1: reproduce it

Find the smallest input that shows the bug. "It breaks on my data" is not a bug
report; "it breaks when the list is empty" is.

```python
def average(nums):
    return sum(nums) / len(nums)

print(average([]))
```

```
ZeroDivisionError: division by zero
```

Now you have a case you can run in two seconds, over and over.

## Step 2: find the wrong assumption

You assumed the list always has something in it. Print the things you assume:

```python
def average(nums):
    print("nums is", nums)
    return sum(nums) / len(nums)
```

The printout confirms it: `nums is []`. The bug is an assumption, not Python.

## Step 3: fix the cause, not the symptom

Wrapping the call in `try/except` hides the crash and returns nothing useful:

```python
try:
    avg = average(nums)
except ZeroDivisionError:
    avg = 0        # silently wrong: 0 is not "no data"
```

The real fix is to decide what an empty list *means*:

```python
def average(nums):
    if not nums:
        return None
    return sum(nums) / len(nums)
```

`None` says "there is no average", which is true. `0` would be a lie.

## Step 4: prove it is fixed

```python
assert average([]) is None
assert average([2, 4]) == 3
```

The assertion for the old bug is what stops it coming back.

## The three habits

- **Print the value you assume.** Most bugs are a variable holding something
  unexpected.
- **Shrink the input** until the bug is obvious.
- **Ask what should happen**, not just what does. Half of all "bugs" are an
  unclear requirement.

> Rubber-duck it: explain the code out loud, line by line. You will often hear
> the mistake before you finish the sentence.
""", {
    "prompt": "first_item() crashes on an empty list. Make it return the string empty instead, so the output is empty.",
    "starter": 'def first_item(items):\n    return items[0]\n\nprint(first_item([]))\n',
    "expected": "empty",
}, 'def first_item(items):\n    if not items:\n        return "empty"\n    return items[0]\n\nprint(first_item([]))')

# ---------------------------------------------------------------- ch19: scripts and tools
lesson("dunder", "Scripts and Tools", "if __name__ == \"__main__\"", """
# if __name__ == "__main__"

You have seen this line. Here is what it is for.

```python
# greet.py
def hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(hello("Ana"))
```

Run it directly:

```
$ python3 greet.py
Hello, Ana!
```

Import it from another file:

```python
import greet
print(greet.hello("Bo"))
```

```
Hello, Bo!
```

The `print(hello("Ana"))` did **not** run on import. Only the function was made
available.

## Why

Every module has a `__name__` variable.

- Run the file directly: `__name__` is `"__main__"`.
- Import it: `__name__` is the module's name, `"greet"`.

So `if __name__ == "__main__":` reads as "am I the program being run, or am I
being imported?"

## Without the guard

```python
# greet.py
def hello(name):
    return f"Hello, {name}!"

print(hello("Ana"))      # runs on every import
```

Now `import greet` prints `Hello, Ana!` as a side effect. In a big project,
importing one module starts doing work -- or worse, deletes a file or connects
to a server -- because some line at the top level ran.

## The shape of a good file

```python
def helper_one():
    ...

def helper_two():
    ...

def main():
    ...                      # the actual program

if __name__ == "__main__":
    main()
```

Imports at the top, definitions in the middle, entry point at the bottom. This
is the layout used by nearly every Python project you will open.

> Even scripts you will never import are easier to test when their logic is in
> functions and only `main()` runs at the bottom.

## Seeing the difference for real

A guard cannot be tested by running the file once -- it behaves the same either
way. The proof is to **import** a file and check what did *not* happen.

The exercise below has `tool.py` next to your program:

```python
# tool.py
def shout(text):
    return text.upper()

if __name__ == "__main__":
    print("tool.py ran directly")
```

If `tool.py` had that `print` at the top level instead, importing it would print.
With the guard, `import tool` prints nothing and you only get the function.
""", {
    "prompt": "tool.py already exists with a __main__ guard. Import it, confirm nothing printed on import, then print tool.shout(\"hi\"). Output: HI",
    "starter": "",
    "expected": "HI",
    "files": {
        "tool.py": 'def shout(text):\n    return text.upper()\n\n\nif __name__ == "__main__":\n    print("tool.py ran directly")\n'
    },
}, 'import tool\n\nprint(tool.shout("hi"))')

lesson("sysargv", "Scripts and Tools", "Command-line Arguments", """
# Command-line Arguments

Every real script takes input from the command line:

```
$ python3 greet.py Ana
Hello, Ana!
```

`sys.argv` is the list of those words.

```python
import sys

print(sys.argv)
```

Running `python3 greet.py Ana` gives:

```
['greet.py', 'Ana']
```

The **first item is always the script name**, so real arguments start at index
`1`. That off-by-one is deliberate: you can check `sys.argv[1:]` to get just the
arguments.

## A working script

```python
import sys

if len(sys.argv) < 2:
    print("usage: python3 greet.py NAME")
    sys.exit(1)

print(f"Hello, {sys.argv[1]}!")
```

Three things worth copying:

- Check `len(sys.argv)` **before** indexing, or you get an `IndexError`.
- Print a usage line so the user knows what to type.
- `sys.exit(1)` returns a non-zero code, which tells the shell it failed.

## Everything is a string

```python
$ python3 add.py 2 3

import sys
a = int(sys.argv[1])     # must convert
b = int(sys.argv[2])
print(a + b)
```

`sys.argv[2]` is `"3"`, not `3`. Forgetting `int()` gives `"23"` instead of `5`.

## Exit codes matter

```python
import sys

sys.exit(0)    # success
sys.exit(1)    # failure
```

Other programs read this number. A script that crashes but exits `0` looks
successful to whatever ran it, which is how broken builds slip through.

> In the exercise you cannot type real command-line arguments, so we set
> `sys.argv` by hand first -- which is exactly what a test does when it checks a
> script.
""", {
    "prompt": "Set sys.argv to [\"greet.py\", \"Ana\"], then print the second element. Output: Ana",
    "starter": "import sys\n\nsys.argv = ['greet.py', 'Ana']\n",
    "expected": "Ana",
}, "import sys\n\nsys.argv = ['greet.py', 'Ana']\nprint(sys.argv[1])")

lesson("venv", "Scripts and Tools", "Virtual Environments and pip", """
# Virtual Environments and pip

`pip` installs packages that are not in the standard library. A **virtual
environment** keeps those packages separate per project.

## Why you need one

Without one, every `pip install` goes into one shared pile. Project A needs
`requests` version 2, project B needs version 3, and they fight.

A virtual environment is a folder holding its own Python packages. Activate it
and `pip install` lands there instead.

## The four commands

```bash
# create it once, in the project folder
python3 -m venv .venv

# activate it (Linux / macOS)
source .venv/bin/activate

# install what you need
pip install requests

# later, leave it
deactivate
```

On Windows the activate line is `.venv\\Scripts\\activate`.

After activating, your prompt shows `(.venv)` so you can tell it is on. `which
python3` should point inside the folder -- if it does not, the activate step
failed.

## Recording what you installed

```bash
pip freeze > requirements.txt
```

That file lists exact versions. Someone else, or future you, recreates the setup
with:

```bash
pip install -r requirements.txt
```

`requirements.txt` belongs in git. `.venv` does **not** -- add it to
`.gitignore`. It is large, machine-specific, and rebuilt from the requirements
file.

## How a program can tell

A venv works by changing `sys.prefix` -- the path Python considers its own
install. Compare the two:

```python
import sys

if sys.prefix != sys.base_prefix:
    print("running inside a virtual environment")
else:
    print("running on the system Python")
```

`base_prefix` is always the *original* interpreter; `prefix` is the current
one. Inside a venv they differ. Tools like `pip` and `pytest` use this to warn
you when you forgot to activate.

## Do not install what you do not need

The standard library is big. Before `pip install`-ing something, check whether
`json`, `csv`, `datetime`, `pathlib` or `urllib` already do it. Every dependency
is code you did not write that you now must keep up to date.

> Only install packages you trust, and pin versions in `requirements.txt`. A
> dependency is also a supply chain.
""", {
    "prompt": "Write check(prefix, base) that returns \"venv\" when they differ and \"system\" when they match. Print check(\"/p/.venv\", \"/p\") then check(\"/usr\", \"/usr\").",
    "starter": 'def check(prefix, base):\n    pass\n\nprint(check("/p/.venv", "/p"))\nprint(check("/usr", "/usr"))\n',
    "expected": "venv\nsystem",
}, 'def check(prefix, base):\n    if prefix != base:\n        return "venv"\n    return "system"\n\nprint(check("/p/.venv", "/p"))\nprint(check("/usr", "/usr"))')


# Progressive hints, keyed by lesson id. Each entry is a list; the Hint button
# reveals them one at a time, so the first nudge stays a nudge.
HINTS = {
    "welcome": [
        "One line of code is enough for this one.",
        "Call print() and put the text inside the brackets, in quotes.",
    ],
    "print": [
        "Each print() call produces one line of output.",
        "You need three separate print() calls, one for each word.",
    ],
    "comments": [
        "Any line starting with # is ignored by Python.",
        "Keep the print() line you were given and add a # comment above it.",
    ],
    "errors": [
        "Count the brackets on that line. Something is unbalanced.",
        "There is an opening ( with no closing ). Add the ) at the end.",
    ],
    "variables": [
        "Create the variable first, then print the variable -- not the text.",
        'Assign a string like city = "Tokyo", then print(city).',
    ],
    "numbers": [
        "The // operator divides and throws away the remainder.",
        "Wrap the whole expression inside print() so you can see the result.",
    ],
    "strings": [
        ".upper() is a method -- it hangs off the value with a dot.",
        "Methods return a new string, so print the result of calling it.",
    ],
    "fstrings": [
        "Put an f right before the opening quote, then wrap variables in curly braces.",
        'The fixed words between the values are " costs " and " dollars".',
    ],
    "input": [
        "n is currently text, not a number. Convert it first.",
        "int() turns a string of digits into a real whole number.",
    ],
    "splitjoin": [
        "split() with no argument breaks the string on whitespace and gives a list.",
        "len() of that list is the number of words.",
    ],
    "strmethods": [
        "strip() removes whitespace from both ends of a string.",
        "It returns a new string, so print the result.",
    ],
    "slicing": [
        "Slicing is [start:stop], and the stop index is excluded.",
        "word[:3] means from the beginning up to, but not including, index 3.",
    ],
    "booleans": [
        "A comparison like > produces a boolean value.",
        "Wrap the comparison inside print() to display it.",
    ],
    "if": [
        "Compare score to 60 using >= so 60 itself counts as a pass.",
        "Do not forget the colon after the condition and the indent inside.",
    ],
    "elif": [
        "Check > 0 first, then < 0, and let else catch everything left.",
        "Zero is neither positive nor negative, so it falls to else.",
    ],
    "for": [
        "range(start, stop) includes start and excludes stop.",
        "To print up to 4 you need range(1, 5).",
    ],
    "while": [
        "Print the number first, then decrease it.",
        "The loop should keep going while n is greater than 0.",
    ],
    "break": [
        "Check whether you have reached 4 before printing it.",
        "The break must come before the print, or 4 gets printed first.",
    ],
    "nested": [
        "The outer loop controls rows; the inner loop builds one row.",
        "Build a string inside the inner loop, then print it once after that loop.",
    ],
    "enumzip": [
        "zip() walks two lists in step, pairing up items.",
        "Unpack each pair in the for line: for name, age in zip(...).",
    ],
    "comprehensions": [
        "The shape is [expression for item in sequence].",
        "The expression is n * n and the sequence is range(1, 4).",
    ],
    "lists": [
        "Indexing starts at 0, not 1.",
        "The second item therefore lives at index 1.",
    ],
    "listops": [
        "append() adds a single item to the end of a list.",
        "Loop over the values, append each one, then print the list.",
    ],
    "listloop": [
        "Start total at 0 before the loop begins.",
        "Add each item to total inside the loop, and print after it ends.",
    ],
    "tuples": [
        "Python can swap two variables in a single line.",
        "a, b = b, a builds a tuple on the right and unpacks it back.",
    ],
    "sets": [
        "A set discards duplicates automatically when you create it.",
        "len(set(nums)) gives you the count of unique values.",
    ],
    "whichcollection": [
        "Turn both lists into sets, then & gives the values in both.",
        "sorted() puts the result back in order so the output is predictable.",
    ],
    "dicts": [
        "A dict literal is written {key: value}.",
        "Read a value by putting the key in square brackets: capitals[\"France\"].",
    ],
    "dictcount": [
        "counts.get(word, 0) + 1 counts without ever raising KeyError.",
        "Then print the value stored under the key \"a\".",
    ],
    "dictloop": [
        ".items() gives you the key and the value together.",
        "Unpack them in the for line: for name, price in prices.items().",
    ],
    "def": [
        "A function is def name(): followed by an indented body.",
        "Defining it does nothing -- you also have to call hello().",
    ],
    "params": [
        "Use return inside the function, not print.",
        "Then print the result of calling square(5) from outside.",
    ],
    "final": [
        "Start with the first item as your current best guess.",
        "Loop the rest, replacing best whenever you find something larger.",
    ],
    "tryexcept": [
        "Put only the risky line inside the try: block.",
        "Catch ValueError specifically -- not a bare except.",
    ],
    "errors2": [
        "items[0] is valid here, so the try block succeeds and prints x.",
        "The except branch only runs if an IndexError actually happens.",
    ],
    "raising": [
        "raise ValueError(...) stops the function immediately.",
        "Return n when the check passes, then print check(5).",
    ],
    "reading": [
        "The file already exists -- check the panel above the code box.",
        "Use a with block around open(), then print what .read() returns.",
    ],
    "writing": [
        "Each line needs its own \\n at the end.",
        "Open the file a second time to read it back, then print it.",
    ],
    "filesum": [
        "Loop over the lines of the file one at a time.",
        "Every line is text, so convert with int() before adding it to total.",
    ],
    "none": [
        "print() inside the function is not the same as returning a value.",
        "Replace print(min(numbers)) with return min(numbers).",
    ],
    "scope": [
        "Inside bump(), assigning to count makes Python treat it as local.",
        "Take a parameter, return n + 1, then assign count = bump(count).",
    ],
    "classes": [
        "__init__ receives self plus the arguments you passed to Book(...).",
        "Store them as self.title = title and self.pages = pages.",
    ],
    "methods": [
        "A method takes self first, then the arguments you call it with.",
        "Add amount to self.balance inside deposit().",
    ],
    "inheritance": [
        "Put the parent in the brackets: class Cat(Animal).",
        "Then define speak(self) in Cat that returns \"Meow\".",
    ],
    "imports": [
        "Bring in the module first with import math.",
        "math.sqrt(81) gives 9.0, and print() it.",
    ],
    "stdlib": [
        "random.seed(42) must come before you pick anything.",
        "Import choice under another name: from random import choice as pick.",
    ],
    "ownmodule": [
        "greeting.py is already in the folder -- look at the panel above the code box.",
        "import greeting, then print(greeting.hello(\"Ana\")).",
    ],
    "sorting": [
        ".sort() changes the list itself and returns None.",
        "Call nums.sort() on its own line, then print(nums).",
    ],
    "keyfunctions": [
        "sorted() accepts a key argument that decides what to compare.",
        "Use key=str.lower so capitals and lowercase sort together.",
    ],
    "lambdas": [
        "max() gives the largest and sum() gives the total.",
        "Print max(scores) first, then sum(scores) on the next line.",
    ],
    "json": [
        "json.dumps() turns a Python value into JSON text.",
        "Print the result of json.dumps(data) -- do not add quotes around it.",
    ],
    "jsonfiles": [
        "json.dump() writes to a file object; json.load() reads one.",
        "Open data.json with \"w\", dump, then reopen and print loaded[\"hits\"].",
    ],
    "csvfiles": [
        "csv.reader gives one list per row, including the header row.",
        "Call next(reader) to skip the header, then print row[0] for each row.",
    ],
    "recursion": [
        "Every recursive function needs a base case that stops it.",
        "If n is 0, return. Otherwise print n, then call count_down(n - 1).",
    ],
    "searching": [
        "Return as soon as you find a match -- do not keep looping.",
        "The condition is len(name) > 3.",
    ],
    "algorithms": [
        "Use n % 3 == 0 to test whether n is a multiple of 3.",
        "Check the divisible-by-3 case before the divisible-by-5 case.",
    ],
    "asserts": [
        "assert expression checks that the expression is true.",
        "Write assert add(2, 3) == 5 and assert add(-1, 1) == 0 before the print.",
    ],
    "tracebacks": [
        "The IndexError says the index is past the end of a 2-item list.",
        "fruits[-1] gives the last item without needing to know the length.",
    ],
    "debugging": [
        "items[0] fails when items is empty -- check for that first.",
        "if not items: return \"empty\", then return items[0].",
    ],
    "dunder": [
        "tool.py already exists -- look at the panel above the code box.",
        "import tool prints nothing thanks to its guard; then print(tool.shout(\"hi\")).",
    ],
    "sysargv": [
        "sys.argv[0] is the script name, so the first real argument is [1].",
        "Print sys.argv[1] to get Ana.",
    ],
    "venv": [
        "The two paths are equal only when you are NOT in a virtual environment.",
        "Return \"venv\" when prefix != base, and \"system\" otherwise.",
    ],
}


# ---------------------------------------------------------------- emit
# Lessons are defined in whatever order is convenient; this list decides the
# order they appear in the course. A chapter missing from here is appended last
# rather than silently dropped.
CHAPTER_ORDER = [
    "Getting Started",
    "Variables and Data",
    "Working with Strings",
    "Making Decisions",
    "Loops",
    "Loop Patterns",
    "Lists",
    "Tuples and Sets",
    "Dictionaries",
    "Functions",
    "None and Scope",
    "Handling Errors",
    "Working with Files",
    "Classes",
    "Modules and the Standard Library",
    "Sorting and Lambdas",
    "Data Formats",
    "Recursion and Algorithms",
    "Testing and Debugging",
    "Scripts and Tools",
]


def build():
    rank = {name: i for i, name in enumerate(CHAPTER_ORDER)}
    ordered = sorted(
        L,
        key=lambda row: (rank.get(row[1], len(CHAPTER_ORDER)), L.index(row)),
    )
    out = []
    for id, chapter, title, body, exercise, solution in ordered:
        entry = {"id": id, "chapter": chapter, "title": title, "body": body}
        if exercise:
            entry["exercise"] = exercise
            entry["exercise"]["hints"] = HINTS.get(id, [])
            entry["exercise"]["solution"] = solution
        out.append(entry)
    return {"lessons": out}


def verify_solutions() -> None:
    """Run every reference solution exactly the way the browser will run it.

    This calls server.run_python() rather than re-implementing the subprocess
    call, so the build check and the real judge can never drift apart. If a
    solution only works under different interpreter flags, the build fails
    here instead of failing for the student.
    """
    import sys
    from pathlib import Path as _Path

    sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
    from server import normalize, run_python  # noqa: E402

    failures = []
    for id, _chapter, _title, _body, exercise, solution in L:
        if not exercise:
            continue
        result = run_python(solution, exercise.get("files") or {})
        got = normalize(result["stdout"])
        want = normalize(exercise["expected"])
        if not result["ok"] or got != want:
            failures.append((id, want, got, (result.get("error") or result["stderr"]).strip()))

    if failures:
        for id, want, got, err in failures:
            print(f"FAIL {id}\n  want: {want!r}\n  got:  {got!r}\n  err:  {err}")
        sys.exit(1)


if __name__ == "__main__":
    # The repo root must be importable before we can reach server.py.
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from server import MAIN_FILE

    # A lesson that seeds main.py would have its file overwritten by the
    # snippet, giving a confusing "file not found" in the browser.
    clashes = [
        i for i, _c, _t, _b, ex, _s in L
        if ex and MAIN_FILE in (ex.get("files") or {})
    ]
    if clashes:
        raise SystemExit(f"lessons seed {MAIN_FILE!r}, which the runner owns: {', '.join(clashes)}")

    verify_solutions()

    # A starter that already passes teaches nothing: the student hits Submit and
    # is told they are done. Empty starters are fine -- the student writes it all.
    from server import normalize, run_python  # noqa: E402  (path set above)

    trivial = []
    for id, _c, _t, _b, ex, _s in L:
        if not ex:
            continue
        starter = (ex.get("starter") or "").strip()
        if not starter:
            continue
        result = run_python(ex["starter"], ex.get("files") or {})
        if result["ok"] and normalize(result["stdout"]) == normalize(ex["expected"]):
            trivial.append(id)
    if trivial:
        sys.exit(f"starter already passes the exercise (student learns nothing): {', '.join(trivial)}")

    missing_hints = [i for i, *_r in L if i not in HINTS]
    if missing_hints:
        sys.exit(f"missing hints for: {', '.join(missing_hints)}")

    thin_hints = [i for i, *_r in L if len(HINTS[i]) < 2]
    if thin_hints:
        sys.exit(f"need 2 hints each: {', '.join(thin_hints)}")

    path = Path(__file__).parent / "lessons.json"
    path.write_text(json.dumps(build(), indent=2, ensure_ascii=False) + "\n", "utf-8")
    n_ex = sum(1 for x in L if x[4])
    n_files = sum(1 for x in L if x[4] and x[4].get("files"))
    n_hints = sum(len(HINTS[i]) for i, *_r in L)
    n_chapters = len({x[1] for x in L})
    print(f"OK: {len(L)} lessons in {n_chapters} chapters, {n_ex} exercises verified "
          f"({n_files} with files), {n_hints} hints -> {path}")
