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
    "starter": 'with open("notes.txt") as f:\n    print(f.read())\n',
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
    "Handling Errors",
    "Working with Files",
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
        out.append(entry)
    return {"lessons": out}


def verify_solutions() -> None:
    """Run every reference solution in a throwaway dir, with its files seeded."""
    import shutil
    import subprocess
    import sys
    import tempfile

    failures = []
    for id, _chapter, _title, _body, exercise, solution in L:
        if not exercise:
            continue
        workdir = tempfile.mkdtemp(prefix="verify-")
        try:
            for name, content in (exercise.get("files") or {}).items():
                target = Path(workdir, name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")

            proc = subprocess.run([sys.executable, "-I", "-c", solution],
                                  capture_output=True, text=True,
                                  timeout=10, cwd=workdir)
            got = proc.stdout.rstrip("\n")
            want = exercise["expected"]
            if proc.returncode != 0 or got != want:
                failures.append((id, want, got, proc.stderr.strip()))
        finally:
            shutil.rmtree(workdir, ignore_errors=True)

    if failures:
        for id, want, got, err in failures:
            print(f"FAIL {id}\n  want: {want!r}\n  got:  {got!r}\n  err:  {err}")
        sys.exit(1)


if __name__ == "__main__":
    verify_solutions()

    path = Path(__file__).parent / "lessons.json"
    path.write_text(json.dumps(build(), indent=2, ensure_ascii=False) + "\n", "utf-8")
    n_ex = sum(1 for x in L if x[4])
    n_files = sum(1 for x in L if x[4] and x[4].get("files"))
    print(f"OK: {len(L)} lessons, {n_ex} exercises verified ({n_files} with files) -> {path}")
