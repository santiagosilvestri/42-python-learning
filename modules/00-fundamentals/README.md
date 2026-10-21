# 00 — Python Fundamentals

> **Status: Ready.** Learn the fundamentals, solve original challenges, and optionally explore reference code after practicing.

[← Chapter index](../README.md) · [Learning path](../../docs/learning-path.md) · [Getting started](../../docs/getting-started.md)

**Goal:** Learn to read, write, and explain small Python programs before building larger ones. Allow about **20–30 minutes** to read this chapter, plus time to experiment.

## 1. Your first instructions

Python executes statements in order. `print()` displays text in the terminal, and `#` begins a comment that Python ignores.

```python
print("Welcome to Python!")
print("One step at a time")  # A comment for the reader
```

Save any example as `scratch.py`, then run `python3 scratch.py` on Linux/macOS or `py scratch.py` on Windows. See [Getting Started](../../docs/getting-started.md) if you haven't configured Python yet.

## 2. Variables and basic types

A variable is a name bound to a value. You don't have to declare its type before using it.

```python
book_title = "The Little Prince"  # str: text
pages = 96                       # int: whole number
rating = 4.5                     # float: decimal number
finished = True                  # bool: True or False

print(f"{book_title}: {pages} pages")
print(type(pages))                # <class 'int'>
```

The `=` symbol **assigns** a value; `==` **compares** two values. Python is case-sensitive: `pages` and `Pages` are different names. Use descriptive `snake_case` names.

### Reading user input

`input()` always returns a string. Convert it if you need a number:

```python
minutes_text = input("How many minutes did you read? ")
minutes = int(minutes_text)
print(f"You read for {minutes + 5} minutes with a five-minute bonus.")
```

Try entering `15`. What happens if you enter `hello` instead? Invalid numeric input raises `ValueError`; you'll learn how to handle errors in [Chapter 02](../02-error-handling/README.md).

## 3. Operators and conditions

Arithmetic operators include `+`, `-`, `*`, `/`, `//` (floor division), and `%` (remainder). Comparisons such as `>=` produce Boolean values. Use `and`, `or`, and `not` to combine conditions.

```python
minutes = 45
sessions = 3
average = minutes / sessions

print(average)             # 15.0
print(minutes % 2)         # 1
print(minutes >= 30)       # True
```

Use `if`, `elif`, and `else` to choose which instructions to run. **Indentation is part of Python syntax**, not just formatting.

```python
minutes = 25

if minutes >= 60:
    print("Long session")
elif minutes >= 20:
    print("Good progress")
else:
    print("Start with a small goal")
```

Only one of these branches runs: Python checks them from top to bottom.

## 4. Repeating work: loops

A `for` loop is useful when you know the values or sequence to iterate over. `range(1, 4)` produces `1`, `2`, and `3` — the stop value is **not included**.

```python
for chapter in range(1, 4):
    print(f"Reading chapter {chapter}")
```

A `while` loop runs **while a condition remains true**. Make sure something can eventually change that condition.

```python
remaining = 3
while remaining > 0:
    print(f"{remaining} pages left")
    remaining -= 1

print("Finished!")
```

Here `remaining -= 1` means `remaining = remaining - 1`. Without it, this particular loop would never end.

## 5. Functions: parameters and return values

A function groups instructions under a reusable name. Parameters receive arguments when the function is called. Use `return` to send a result back to the caller; `print()` only displays it.

```python
def reading_goal(minutes: int, target: int) -> bool:
    return minutes >= target


def main() -> None:
    completed = reading_goal(35, 30)
    print(f"Goal reached: {completed}")


if __name__ == "__main__":
    main()
```

`int`, `bool`, and `None` above are **type annotations** that communicate intent; Python does not automatically enforce them at runtime. The `if __name__ == "__main__":` pattern runs `main()` when this file is executed directly.

## 6. Recursion: a function calling itself

A recursive function solves a problem by working on a smaller version of it. It needs a **base case** that stops further calls.

```python
def countdown(number: int) -> None:
    if number <= 0:       # Base case
        print("Go!")
        return

    print(number)
    countdown(number - 1)


countdown(3)
```

Output:

```text
3
2
1
Go!
```

Compare this with a loop: both can repeat work, but a simple countdown is usually easier to write iteratively. Recursion is most useful when a problem naturally contains smaller versions of itself. Very deep recursion can hit Python's recursion limit.

## 7. Putting the ideas together

This complete program combines a function, variables, a loop, arithmetic, a return value, and a condition. Copy it into a file and run it.

```python
def total_reading_time(days: int, minutes_per_day: int) -> int:
    total = 0
    for _ in range(days):
        total += minutes_per_day
    return total


def main() -> None:
    days = 4
    daily_minutes = 15
    total = total_reading_time(days, daily_minutes)

    if total >= 60:
        print(f"Goal reached: {total} minutes")
    else:
        print(f"Keep going: {total} minutes")


if __name__ == "__main__":
    main()
```

**Expected output:** `Goal reached: 60 minutes`

Before running it again, **predict** what will happen if you change `days` to `2`. Then modify `daily_minutes` and explain why the result changes. The loop is intentionally explicit for learning; in a real application, multiplication would also calculate this total.

## Common mistakes to watch for

| Mistake | Why it matters |
| :--- | :--- |
| Using `=` in an `if` condition | Use `==` when comparing values. |
| Treating `input()` as a number | Convert the returned string before doing numeric arithmetic. |
| Assuming `range(1, 4)` includes `4` | The end of a `range` is excluded. |
| Mixing indentation levels | Blocks must be indented consistently. |
| Using `print()` instead of `return` | Printing doesn't pass a result back to the caller. |
| Writing recursion without a base case | Calls continue until Python raises an error. |

## Before you practice

Make sure you can explain the difference between `=`, `==`, and `return`; trace a short `if` statement and a loop; and identify the base case in `countdown()`. **You do not need to memorize everything.** You should be able to run the examples and explain what they do.

## 8. Practice: build it yourself

**Do these before opening the reference code.** The tasks below are original warm-ups rather than project instructions. Write each one in a new `.py` file, test it with several values, and explain your choices.

| Level | Challenge | Requirements and example |
| :--- | :--- | :--- |
| 1 · Warm-up | **Temperature converter** | Write `to_fahrenheit(celsius: float) -> float`. Formula: `celsius * 9 / 5 + 32`. Check `0 → 32` and `100 → 212`. |
| 2 · Conditions | **Score category** | Write `score_category(score: int) -> str`: return `"excellent"` for 80–100, `"good"` for 50–79, and `"keep practicing"` for 0–49. Decide how to treat values outside 0–100. |
| 3 · Loops | **Even-number total** | Write `sum_evens(limit: int) -> int` that adds even numbers from 1 through `limit`. Check `6 → 12` and `1 → 0`. |
| 4 · Recursion | **Sum from one to n** | Write `sum_to(n: int) -> int` recursively, with a base case for `0`. Check `sum_to(4) → 10`. Start with non-negative inputs. |
| 5 · Mini-project | **Weekly study tracker** | Ask for minutes studied over 3 days, calculate the total and average, then display whether the total reaches 120 minutes. Separate the calculation from the printing. |

**Tips:** Start with a function signature, try ordinary values and boundaries, and compare what you *predicted* with what Python actually does. If your code fails, read the error before changing anything.

## 9. Knowledge check

Try answering without running code first:

1. Why does `input()` need conversion when you want a number?
2. What is the difference between `print(value)` and `return value`?
3. Which numbers are produced by `range(2, 7)`?
4. Do Python type annotations prevent wrong argument types at runtime automatically?
5. What happens if a recursive function never reaches its base case?

**Predict the output:**

```python
points = 0
for number in range(1, 5):
    if number % 2 == 0:
        points += number
print(points)
```

**Spot the bug:** Why does this loop never finish when `limit` is positive? How would you fix it?

```python
def show_numbers(limit: int) -> None:
    number = 0
    while number < limit:
        print(number)
```

## 10. Optional: reference implementations

<details>
<summary>Show reference code links (open only after trying the challenges)</summary>

These are personal, small programs for inspecting basic syntax. **They are not solutions to the five original challenges above** and are not a substitute for implementing your own exercises. Their function bodies are preserved from the author's examples; an `if __name__ == "__main__":` entry point was added to make each file runnable directly.

| Concept | Example |
| :--- | :--- |
| Printing | [`ft_hello_garden.py`](reference/ft_hello_garden.py) |
| Text input | [`ft_garden_name.py`](reference/ft_garden_name.py) |
| Numeric input and multiplication | [`ft_plot_area.py`](reference/ft_plot_area.py) |
| Adding values | [`ft_harvest_total.py`](reference/ft_harvest_total.py) |
| Comparisons and conditions | [`ft_plant_age.py`](reference/ft_plant_age.py) |
| Conditional reminders | [`ft_water_reminder.py`](reference/ft_water_reminder.py) |
| Iteration | [`ft_count_harvest_iterative.py`](reference/ft_count_harvest_iterative.py) |
| Recursion | [`ft_count_harvest_recursive.py`](reference/ft_count_harvest_recursive.py) |
| Parameters and branching | [`ft_seed_inventory.py`](reference/ft_seed_inventory.py) |

From the repository root, run for example:

```bash
python3 modules/00-fundamentals/reference/ft_hello_garden.py
python3 modules/00-fundamentals/reference/ft_seed_inventory.py
```

Other examples ask for input in the terminal. Try changing an argument or entering a different value, then explain the result. Numeric examples assume valid numeric input; handling invalid input is a topic for [Chapter 02](../02-error-handling/README.md). The recursive example is intended for small input values.

</details>

### Ready for the next chapter?

You should now be able to write a short function, explain its return value, trace a loop, use an `if` statement, and identify a recursive base case. If any of those are still unclear, revisit the examples and attempt one challenge again before moving on.

---

[← All chapters](../README.md) · [Learning path](../../docs/learning-path.md) · [01 — Object-Oriented Programming →](../01-oop/README.md)
