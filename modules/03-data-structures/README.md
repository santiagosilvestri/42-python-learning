# 03 — Data Structures

> **Status: In progress.** The concept lesson is ready. Original practice challenges and optional reference programs will be added in the next update.

[← Chapter index](../README.md) · [Learning path](../../docs/learning-path.md) · [Getting started](../../docs/getting-started.md) · [← 02 — Error Handling](../02-error-handling/README.md)

**Goal:** Choose a suitable collection, transform data clearly, and process values one at a time when you do not need to store everything. Allow about **25–35 minutes** for this lesson.

Before starting, review [loops and functions in Chapter 00](../00-fundamentals/README.md) and [exceptions in Chapter 02](../02-error-handling/README.md).

## 1. Choosing a collection

Python provides several useful built-in collections. Each solves a different problem.

| Type | Example | Best when you need... |
| :--- | :--- | :--- |
| `list` | `[10, 20, 30]` | An ordered, changeable sequence that may contain duplicates. |
| `tuple` | `(10, 20)` | A fixed-length collection whose elements should not be reassigned. |
| `set` | `{"red", "blue"}` | Unique values, membership tests, and set operations. |
| `dict` | `{"red": 2}` | A lookup from unique keys to values. |

Lists and tuples preserve element order. Dictionaries preserve insertion order; sets do **not** guarantee a useful iteration order. Both lists and dictionaries can be changed after creation. A tuple cannot have its elements reassigned, but a mutable object inside a tuple may still change.

**Rule of thumb:** Choose your collection based on what operations you need, not just how the data looks.

## 2. Lists: store, access, and transform values

Lists are useful when you have a sequence of items that can grow or change.

```python
minutes = [25, 40, 15]
minutes.append(30)

print(minutes[0])       # 25
print(minutes[-1])      # 30
print(minutes[1:3])     # [40, 15]
print(len(minutes))     # 4
print(sum(minutes))     # 110
```

- Index `0` refers to the first element; `-1` refers to the last.
- A slice such as `items[1:3]` includes index `1`, but excludes index `3`.
- `append()` changes the list **in place** and returns `None`.
- `sum()`, `min()`, and `max()` can help summarize numeric data. `min()` and `max()` require a nonempty iterable unless you supply a default.

### Passing data through command-line arguments

A program can receive values after its filename. Python makes them available in `sys.argv`, which is a **list of strings**.

Save the following example as `arguments.py`:

```python
import sys


def main() -> None:
    values = sys.argv[1:]
    print(f"Received {len(values)} values")
    for index, value in enumerate(values, start=1):
        print(f"{index}: {value}")


if __name__ == "__main__":
    main()
```

Run it with:

```bash
python3 arguments.py apple banana
```

**Expected output:**

```text
Received 2 values
1: apple
2: banana
```

`sys.argv[0]` is normally the script name; the slice `[1:]` excludes it. Even if an argument looks like a number, it arrives as text. Convert it with `int()` or `float()` when needed, and handle invalid input using the ideas from [Chapter 02](../02-error-handling/README.md).

## 3. Tuples and unpacking

A tuple is useful for a small group of related values with a known structure, such as a coordinate or a color.

```python
position = (3, 4, 0)
x, y, z = position

print(x)                # 3
print(position[1])      # 4
print(f"Height: {z}")  # Height: 0
```

**Unpacking** assigns elements to separate variables. The number of targets must match the number of elements, unless you use starred unpacking.

```python
from math import dist


def distance(a: tuple[float, float],
             b: tuple[float, float]) -> float:
    return dist(a, b)


print(distance((0, 0), (3, 4)))  # 5.0
```

The type hint `tuple[float, float]` describes a tuple with exactly two floating-point positions. Python's type hints document expectations and support static tools; they do not automatically validate inputs at runtime.

## 4. Sets: unique values and relationships

A set stores **distinct elements**. It is particularly useful when you want to check which values appear in different groups.

```python
team_a = {"git", "python", "linux"}
team_b = {"python", "docker", "linux"}

print(team_a | team_b)  # Union: all distinct skills
print(team_a & team_b)  # Intersection: shared skills
print(team_a - team_b)  # Difference: only team A
print("git" in team_a)  # True
```

Set output order can vary, so don't rely on the printed order. A set cannot contain mutable, unhashable values such as lists; its elements must be hashable. To create an empty set, use `set()`—`{}` creates an empty dictionary.

**Try it:** Which operation would you use to find attendees who signed up for *both* workshops?

## 5. Dictionaries: keys, values, and updates

A dictionary maps each **unique key** to a value. Lookups are convenient when you know what a value should be called.

```python
supplies = {"paper": 12, "pens": 5}
supplies["paper"] += 3
supplies.update({"folders": 2})

print(supplies["paper"])           # 15
print(supplies.get("staples", 0))   # 0

for name, quantity in supplies.items():
    print(f"{name}: {quantity}")
```

Useful methods include:

- `keys()` — view the dictionary's keys.
- `values()` — view its values.
- `items()` — view `(key, value)` pairs for iteration.
- `get(key, default)` — access a value without raising `KeyError` for a missing key.
- `update()` — add or replace entries from another mapping.

`dict[key]` raises `KeyError` when the key is missing; use `get()` when absence is an expected case. Dictionary keys must be hashable, while values can be of many different types.

## 6. Comprehensions: create collections clearly

A **comprehension** can build a new collection from an iterable, optionally filtering elements.

```python
scores = [12, 7, 18, 5]

passed = [score for score in scores if score >= 10]
labels = {score: "pass" if score >= 10 else "retry"
          for score in scores}
unique_last_digits = {score % 10 for score in scores}

print(passed)              # [12, 18]
print(labels[7])           # retry
print(len(unique_last_digits))  # 4
```

These are **list**, **dictionary**, and **set** comprehensions. They return collections immediately. Use them when the transformation is short and readable. Prefer an ordinary `for` loop for complicated logic or multiple side effects.

A dictionary comprehension produces one value for each distinct key. If the same key is generated more than once, the later value replaces the earlier one.

## 7. Iterables, iterators, and generators

An **iterable** can provide an iterator, so you can use it in a `for` loop. An **iterator** supplies values one at a time through `next()`. A **generator function** uses `yield` to create an iterator that resumes from where it paused.

```python
from collections.abc import Iterator


def countdown(start: int) -> Iterator[int]:
    while start > 0:
        yield start
        start -= 1


numbers = countdown(3)
print(next(numbers))  # 3
print(next(numbers))  # 2
print(list(numbers))  # [1]
```

Calling `countdown(3)` creates a generator; it does not run the function body immediately. Each `next()` resumes it until the next `yield`. A `for` loop calls `next()` automatically and stops when the iterator is exhausted. Calling `next()` again on an exhausted generator raises `StopIteration`.

A generator is helpful for **lazy processing**, when values can be produced as needed rather than stored all at once.

```python
from collections.abc import Iterator


def even_numbers(limit: int) -> Iterator[int]:
    for number in range(limit):
        if number % 2 == 0:
            yield number


for value in even_numbers(6):
    print(value, end=" ")  # 0 2 4 
print()
```

A generator usually avoids building a complete result list, but it is not automatically faster. Use a list when you need to reuse or index all values; use a generator when one-pass processing is enough.

## 8. Putting it together

This small reading tracker combines a list, tuples, a dictionary, and a set—without creating a complex class.

```python
sessions = [("Python", 25), ("Linux", 30), ("Python", 15)]
minutes_by_topic: dict[str, int] = {}

for topic, minutes in sessions:
    minutes_by_topic[topic] = minutes_by_topic.get(topic, 0) + minutes

topics = {topic for topic, _ in sessions}

print(minutes_by_topic)  # {'Python': 40, 'Linux': 30}
print(len(topics))        # 2
```

Notice how each structure has a purpose: the list keeps all sessions, each tuple holds a pair, the dictionary aggregates totals by topic, and the set counts distinct topics.

## Common mistakes

| Mistake | Better approach |
| :--- | :--- |
| Using `values = values.append(x)` | Call `values.append(x)`; the method returns `None`. |
| Accessing `items[0]` when a list may be empty | Check the list first. |
| Expecting a set to keep a predictable order | Sort it explicitly when order matters. |
| Treating `sys.argv` elements as numbers | Parse strings and handle conversion errors. |
| Accessing a missing dictionary key directly | Consider `get()` when missing values are normal. |
| Expecting to iterate a finished generator again | Create a new generator or materialize the data deliberately. |
| Writing a long, hard-to-read comprehension | Use a clear `for` loop. |

## Knowledge check

Before running the code, explain these questions in your own words:

1. When would you choose a tuple rather than a list?
2. What does `sys.argv[1:]` contain? Why is every argument a string?
3. How do union, intersection, and difference behave on sets?
4. What is the difference between `inventory["missing"]` and `inventory.get("missing", 0)`?
5. Why might a generator use less memory than building a list?
6. What happens when you call `next()` on an exhausted generator?

**Predict the output:**

```python
numbers = [2, 3, 2, 4]
print(len(set(numbers)))
print([value * 2 for value in numbers if value > 2])
```

## 9. Practice: build it yourself

Try these **five original challenges** without opening the reference programs. You can write each solution in a separate file on your computer. Start small, test different inputs, and explain why you chose each collection.

| Level | Challenge | Your goal |
| :--- | :--- | :--- |
| 1 · Lists | **Playlist explorer** | Read song titles from the command line. Print the number of titles, the first and last title when present, and a numbered playlist. Test zero, one, and several titles, including titles containing spaces. |
| 2 · Tuples | **Delivery route** | Store a sequence of two-dimensional checkpoints as `(x, y)` tuples. Unpack each checkpoint and calculate the total *Manhattan distance* (the sum of absolute changes in `x` and `y`) between consecutive checkpoints. |
| 3 · Sets | **Workshop groups** | Given the attendees of two workshops, report who joined either workshop, who joined both, and who joined only the first one. Explain why duplicates should not affect your results. |
| 4 · Dictionaries | **Library loans** | Start with a list of borrowed book genres. Build a dictionary counting how often each genre appears, then print a summary ordered alphabetically. Handle an empty reading history. |
| 5 · Mini-project | **Study activity report** | Store `(topic, minutes)` records, build totals by topic, and use a comprehension to select topics with at least 30 minutes. Write a generator that yields each selected topic one at a time. |

**Practice tip:** Try at least two edge cases for each challenge. Empty collections, repeated values, and a single element often reveal bugs earlier than large examples.

### Debugging challenge

This code is intended to collect a new score and print the updated list. Why does it fail, and how would you fix it without replacing the original list?

```python
scores = [12, 18]
scores = scores.append(24)
print(scores[-1])
```

### Predict the output

What will be printed? Explain the role of `set()`, unpacking, and dictionary lookup.

```python
records = [("A", 2), ("B", 3), ("A", 4)]
totals: dict[str, int] = {}
for name, points in records:
    totals[name] = totals.get(name, 0) + points
print(len(set(name for name, _ in records)))
print(totals["A"])
```

## 10. Knowledge check

Answer these questions *before* running code or consulting examples:

1. How does `sys.argv[1:]` differ from `sys.argv`? How would you convert numeric arguments safely?
2. Which is a better choice for a changeable collection: a list or a tuple? Why?
3. What is tuple unpacking, and what happens when the number of values does not match the number of targets?
4. How do union, intersection, and difference behave for sets? When would you use each?
5. What is the difference between `mapping[key]` and `mapping.get(key, default)`?
6. What does `yield` do, and why can a generator be useful for processing many values?
7. When is a comprehension clearer than a `for` loop, and when is a normal loop preferable?

## 11. Optional: reference programs

<details>
<summary>Show reference programs (open after independent practice)</summary>

These are the author's reference implementations showing related Python features. **They are not solutions to the five challenges above.** Try the examples in this lesson first, then read one program and explain what each collection is doing. Some demonstrations produce random output.

| Concept | Program |
| :--- | :--- |
| Command-line arguments and list iteration | [`ft_command_quest.py`](reference/ft_command_quest.py) |
| Working with numeric lists | [`ft_score_analytics.py`](reference/ft_score_analytics.py) |
| Tuples and distance calculations | [`ft_coordinate_system.py`](reference/ft_coordinate_system.py) |
| Set operations | [`ft_achievement_tracker.py`](reference/ft_achievement_tracker.py) |
| Dictionaries and summaries | [`ft_inventory_system.py`](reference/ft_inventory_system.py) |
| Generators and streaming values | [`ft_data_stream.py`](reference/ft_data_stream.py) |
| List and dictionary comprehensions | [`ft_data_alchemist.py`](reference/ft_data_alchemist.py) |

From the repository root, you can run, for example:

```bash
python3 modules/03-data-structures/reference/ft_command_quest.py "Hello World" 42
python3 modules/03-data-structures/reference/ft_score_analytics.py 12 24 36
python3 modules/03-data-structures/reference/ft_inventory_system.py paper:3 pens:5
```

`ft_coordinate_system.py` asks for interactive input. `ft_data_stream.py` prints over 1,000 lines, so you may want to redirect its output to a local text file when exploring it. The set and comprehension demonstrations include random values, so their output will vary.

</details>

### Ready for the next chapter?

You should be able to select a suitable collection, iterate over arguments, unpack a tuple, compare sets, use dictionaries to count values, write a readable comprehension, and explain how a generator resumes. If you can complete the practice challenges without copying a reference program, you have a useful foundation for building your own solutions.

---

[← 02 — Error Handling](../02-error-handling/README.md) · [Chapter index](../README.md) · [04 — Files and I/O →](../04-files-io/README.md)
