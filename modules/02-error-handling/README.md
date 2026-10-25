# 02 — Error Handling

> **Status: In progress.** The lesson and examples are available. Original practice challenges and optional reference code will be added in the next update.

[← Chapter index](../README.md) · [Learning path](../../docs/learning-path.md) · [Getting started](../../docs/getting-started.md) · [← 01 — Object-Oriented Programming](../01-oop/README.md)

**Goal:** Learn to handle expected failures without hiding programming mistakes. Allow about **20–25 minutes** to read the lesson and try the examples.

Before starting, review [functions and basic types](../00-fundamentals/README.md). You will also use [classes and inheritance](../01-oop/README.md) to define your own exceptions.

## 1. What is an exception?

An **exception** is an object that signals a problem while a program is running. For example, `int("hello")` raises a `ValueError` because the string cannot be converted to an integer.

```python
text = "42"
number = int(text)
print(number + 1)  # 43
```

Now try replacing `"42"` with `"hello"`. Without error handling, Python stops executing that part of the program and prints a traceback. The traceback helps you locate the failing operation.

Different problems have different exception types:

| Exception | Typical cause |
| :--- | :--- |
| `ValueError` | A value is not valid for an operation, such as `int("hello")`. |
| `TypeError` | An operation receives an incompatible type, such as `"a" + 1`. |
| `ZeroDivisionError` | A number is divided by zero. |
| `FileNotFoundError` | A program tries to open a file that does not exist. |
| `KeyError` | A dictionary lookup requests a missing key. |

An exception is **not** the same as returning a special value. Raising an exception interrupts normal execution until a matching handler is found.

## 2. Handling expected errors with `try` and `except`

Put an operation that may fail inside `try`. An `except` block runs if a matching exception occurs.

```python
def parse_age(text: str) -> int:
    return int(text)


for raw_age in ("21", "unknown", "35"):
    try:
        age = parse_age(raw_age)
        print(f"Age: {age}")
    except ValueError:
        print(f"Invalid age: {raw_age}")
```

**Expected output:**

```text
Age: 21
Invalid age: unknown
Age: 35
```

The program keeps going because the invalid value is handled. Notice that the `try` block only contains the work we expect might fail. Catching **specific** exceptions is safer than silently swallowing every error.

## 3. Handling different exception types

One `try` block can have multiple `except` clauses. Python uses the **first matching handler**.

```python
def calculate_share(total: str, people: str) -> float:
    return int(total) / int(people)


for total, people in (("60", "3"), ("60", "0"), ("many", "3")):
    try:
        result = calculate_share(total, people)
        print(f"Share: {result}")
    except ValueError as error:
        print(f"Invalid number: {error}")
    except ZeroDivisionError:
        print("The number of people must not be zero")
```

The two error types represent **different problems**. Using `as error` gives you access to the exception object and its message.

If you catch a parent exception class, such as `Exception`, it will also catch its subclasses. Place more specific handlers before general ones, and avoid a broad handler unless you have a clear reason to use it.

## 4. Raising exceptions with `raise`

Python raises some exceptions automatically. You can also use `raise` to reject invalid data according to your program's rules.

```python
def set_volume(level: int) -> int:
    if not 0 <= level <= 100:
        raise ValueError("Volume must be between 0 and 100")
    return level


for value in (30, 150):
    try:
        print(f"Volume set to {set_volume(value)}")
    except ValueError as error:
        print(f"Cannot set volume: {error}")
```

**Expected output:**

```text
Volume set to 30
Cannot set volume: Volume must be between 0 and 100
```

A helpful error message should explain **what was wrong**. Do not raise an exception for ordinary, expected choices when a simple return value is clearer.

## 5. `else` and `finally`

The complete error-handling structure can include two additional blocks:

- `else` runs **only if the `try` block finishes without an exception**.
- `finally` runs when leaving the structure, whether an exception occurred or not. It also runs when a `return` exits the `try` or `except` block.

```python
def describe_percentage(text: str) -> None:
    print("Starting calculation")
    try:
        number = int(text)
        percentage = 100 / number
    except ValueError:
        print("Enter a whole number")
    except ZeroDivisionError:
        print("The number must not be zero")
    else:
        print(f"Result: {percentage}")
    finally:
        print("Calculation finished")


describe_percentage("4")
describe_percentage("0")
```

Here, `else` prints the result only for valid input, while `finally` prints the closing message in both calls. In real programs, cleanup may mean closing a resource or releasing a lock. When working with files, prefer a `with` statement when possible; [Chapter 04](../04-files-io/README.md) explains why.

### What if the function returns early?

```python
def check_code(code: str) -> bool:
    try:
        if not code:
            return False
        return True
    finally:
        print("Check complete")


print(check_code(""))
```

**Expected output:**

```text
Check complete
False
```

`finally` runs **before** the return is completed. Don't put another `return` inside `finally`: it can unexpectedly replace the original result or hide an exception.

## 6. Custom exceptions and inheritance

When built-in exception names are not specific enough, define your own by subclassing `Exception`. Related exceptions can share a parent class.

```python
class BookingError(Exception):
    pass


class SeatUnavailableError(BookingError):
    pass


def reserve_seats(available: int, requested: int) -> int:
    if requested <= 0:
        raise BookingError("Request at least one seat")
    if requested > available:
        raise SeatUnavailableError("Not enough seats available")
    return available - requested


for requested in (2, 8):
    try:
        remaining = reserve_seats(5, requested)
        print(f"Remaining seats: {remaining}")
    except SeatUnavailableError as error:
        print(f"Cannot reserve: {error}")
```

`SeatUnavailableError` **is a** `BookingError`, which **is an** `Exception`. Therefore `except BookingError` could also catch `SeatUnavailableError`. The example uses the more specific handler to make the expected failure clear.

The `pass` statements are intentional: an exception class often needs no extra methods. Messages passed when raising it are stored by the inherited exception behavior.

## 7. Choosing where to handle an error

A useful rule is: **raise where you recognize a problem; catch where you know what to do about it**.

- A parsing function can raise `ValueError` when an input cannot be converted.
- A user-facing function can catch it and ask for a different input.
- An unexpected programming error should usually remain visible while you debug, rather than being silently ignored.

Avoid this pattern:

```python
try:
    value = int("invalid")
except Exception:
    pass  # The failure disappears, making debugging difficult.
```

Also avoid wrapping an entire program in one large `try` block. Smaller blocks make it clearer **which operation may fail** and **how to recover**.

## Common mistakes to watch for

| Mistake | Better approach |
| :--- | :--- |
| Catching `Exception` for every failure | Handle the specific errors you expect. |
| Using `except: pass` | Report or handle expected errors; don't hide bugs. |
| Catching a parent class before its child | Put the more specific handler first. |
| Raising errors without useful messages | Describe the invalid value or required condition. |
| Assuming `finally` runs only on errors | Remember that it also runs after successful execution and before an early return. |
| Returning from `finally` | Avoid overriding returns or suppressing exceptions. |

## Check your understanding

Try answering these questions before running the examples again:

1. What happens when `int("hello")` is executed without a handler?
2. Why might two separate `except` blocks be clearer than one broad handler?
3. When should a function raise `ValueError` instead of returning a value?
4. What is the difference between `else` and `finally`?
5. Why can a parent exception handler catch a custom child exception?
6. What makes an error message useful to someone debugging a program?

**Predict the output:**

```python
def read_level(text: str) -> None:
    try:
        level = int(text)
    except ValueError:
        print("Invalid")
    else:
        print(f"Level: {level}")
    finally:
        print("Done")


read_level("3")
read_level("high")
```

**Next update:** You'll put these concepts into practice with original challenges and optional reference programs. Until then, try changing the inputs in the examples and predict which blocks will run.

---

[← 01 — Object-Oriented Programming](../01-oop/README.md) · [Chapter index](../README.md) · [03 — Data Structures →](../03-data-structures/README.md)
