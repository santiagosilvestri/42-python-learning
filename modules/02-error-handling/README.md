# 02 — Error Handling

> **Status: Ready.** Learn the concepts, practice independently, then explore the optional reference programs.

[← Chapter index](../README.md) · [Learning path](../../docs/learning-path.md) · [Getting started](../../docs/getting-started.md) · [← 01 — Object-Oriented Programming](../01-oop/README.md)

**Goal:** Learn to handle expected failures without hiding programming mistakes. Allow about **20–25 minutes** for the lesson and extra time to solve the practice challenges.

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

## 8. Practice: build it yourself

**Try these original challenges before opening the reference code.** Create your own `.py` files, test success and failure cases, and explain why you catch each exception. The reference programs below demonstrate related concepts, but do **not** solve these challenges.

| Level | Challenge | Your goal |
| :--- | :--- | :--- |
| 1 · Conversion | **Reading minutes** | Write `parse_minutes(text: str) -> int`. Convert a string to an integer, reject negative values with `ValueError`, and display a friendly message when parsing fails. Try `"30"`, `"unknown"`, and `"-5"`. |
| 2 · Multiple errors | **Split a bill** | Write `split_bill(total: str, guests: str) -> float`. Convert both inputs and divide the amount. Handle invalid numbers and zero guests with different messages, and continue processing the next pair. |
| 3 · Custom errors | **Ticket checkout** | Create `TicketError` and a subclass `SoldOutError`. Write a function that raises `SoldOutError` when a request exceeds the remaining tickets. Show that a handler for `TicketError` can catch the child exception. |
| 4 · Cleanup | **Study session** | Write `run_session(duration: str) -> None` that prints an opening message, converts the duration to a positive integer, and always prints a closing message using `finally`. Try valid and invalid input. |
| 5 · Mini-project | **Workshop registration** | Combine conversion, validation, a custom exception and `finally`. Process several seat requests independently, so one invalid registration does not stop later ones. Explain which errors your program catches and which ones it deliberately leaves visible. |

**Tips:** Catch errors where you know how to recover. Keep `try` blocks small. Test boundary values, not just one valid value. A custom exception is useful when the caller needs to distinguish a domain-specific failure from a general input error.

### Debugging challenge

This function catches invalid integers but still fails for one important input. Which input is it? Fix the code by handling that error explicitly without hiding unrelated programming mistakes.

```python
def safe_average(total: str, count: str) -> float:
    try:
        return int(total) / int(count)
    except ValueError:
        return 0.0


print(safe_average("12", "0"))
```

## 9. Knowledge check

Explain these ideas before consulting the programs below:

1. What happens when `int("hello")` runs without an exception handler?
2. Why is catching `ValueError` different from catching `ZeroDivisionError`?
3. When should a function use `raise` rather than return a normal result?
4. When do `else` and `finally` run in a `try` statement?
5. How can a handler for a parent exception catch its subclass?
6. Why does `except Exception: pass` often make debugging harder?
7. If you put `return` inside `try`, does `finally` still execute?

**Predict the output before running this code:**

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

## 10. Optional: reference implementations

<details>
<summary>Show reference programs (open after independent practice)</summary>

These are the author's small programs illustrating exception handling. **They are not solutions to the five original challenges above.** Read one at a time, predict which errors will occur, run the program, and change an input to see how the handler responds.

| Concept | Example |
| :--- | :--- |
| Converting input and catching `ValueError` | [`ft_first_exception.py`](reference/ft_first_exception.py) |
| Rejecting out-of-range input with `raise` | [`ft_raise_exception.py`](reference/ft_raise_exception.py) |
| Handling several built-in exception types | [`ft_different_errors.py`](reference/ft_different_errors.py) |
| Creating and catching an exception hierarchy | [`ft_custom_errors.py`](reference/ft_custom_errors.py) |
| Running cleanup with `finally`, including early `return` | [`ft_finally_block.py`](reference/ft_finally_block.py) |

From the repository root, run for example:

```bash
python3 modules/02-error-handling/reference/ft_first_exception.py
python3 modules/02-error-handling/reference/ft_finally_block.py
```

Some examples **intentionally trigger exceptions** so that their handlers can demonstrate recovery. In `ft_different_errors.py`, an invalid string/integer addition is deliberate; a static type checker can flag that demonstration even though the script catches the resulting `TypeError` at runtime.

</details>

### Ready for the next chapter?

You should be able to convert input safely, recognize different exception types, choose when to raise or catch an error, define a custom exception, and explain why cleanup belongs in `finally`. If you can independently solve challenges 1–4 and reason about challenge 5, you have a useful foundation for handling failures in larger projects.

---

[← 01 — Object-Oriented Programming](../01-oop/README.md) · [Chapter index](../README.md) · [03 — Data Structures →](../03-data-structures/README.md)
