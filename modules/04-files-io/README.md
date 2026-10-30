# 04 — Files and I/O

> **Status: In progress.** The concept lesson is ready. Original practice challenges and optional reference programs will be added in the next update.

[← Chapter index](../README.md) · [Learning path](../../docs/learning-path.md) · [Getting started](../../docs/getting-started.md) · [← 03 — Data Structures](../03-data-structures/README.md)

**Goal:** Read and write text files safely, understand standard streams, and handle common I/O failures. Allow about **25–30 minutes** for this lesson.

Before starting, review [functions and command-line arguments](../00-fundamentals/README.md) and [exceptions](../02-error-handling/README.md).

## 1. Files, paths, and streams

A **file** stores information that a program can read later, even after the program exits. A **path** identifies where the file is located. A relative path such as `notes.txt` is resolved from the program's **current working directory**, which may be different from the folder containing your script.

A **stream** is a way to read or write a sequence of data. An open file is one kind of stream. Your terminal also provides standard streams for input, normal output, and errors; we will use them later.

Opening a file returns a file object. When you finish with it, you need to close it so its resources can be released.

## 2. Open, read, and close a text file

The basic pattern is `open()` → `read()` → `close()`. Here is a complete example: the first part creates a small sample file, and the second part reads it manually.

```python
with open("demo_read.txt", "w", encoding="utf-8") as sample:
    sample.write("Python is fun!\nSecond line\n")

file = open("demo_read.txt", "r", encoding="utf-8")
try:
    content = file.read()
    print(content, end="")
finally:
    file.close()

print(file.closed)  # True
```

**Expected output:**

```text
Python is fun!
Second line
True
```

- `"r"` means **read**. The file must already exist.
- `read()` returns the whole file as a string. For a very large file, this can use a lot of memory.
- `print(content, end="")` avoids adding an extra newline if the content already ends with one.
- The `finally` block runs even if reading raises an exception, so the file is closed.
- `file.closed` reports whether the file object is closed.

We used `with` to create the sample file. In everyday code, you should also prefer it when **reading**, as shown below.

## 3. Choose the right file mode

| Mode | Purpose | Important behavior |
| :--- | :--- | :--- |
| `"r"` | Read an existing file | Raises `FileNotFoundError` if it is missing. |
| `"w"` | Write a file | **Overwrites** an existing file (or creates one). |
| `"a"` | Append to a file | Adds content at the end (or creates one). |
| `"x"` | Create a new file | Raises `FileExistsError` if it already exists. |

Text files use a character **encoding**. For our examples, `encoding="utf-8"` makes the choice explicit. Reading a file using the wrong encoding can raise `UnicodeError` or produce incorrect text.

**Important:** These examples create local `demo_*.txt` files in your current working directory. Run them in a scratch folder and never test `"w"` on a file you want to keep.

## 4. Read a file one line at a time

With `with open(...) as file`, Python closes the file when you leave the block, including when an exception occurs inside it.

```python
with open("demo_lines.txt", "w", encoding="utf-8") as file:
    file.write("alpha\nbeta\ngamma\n")

with open("demo_lines.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        clean_line = line.rstrip("\n")
        print(f"{line_number}: {clean_line}")
```

**Expected output:**

```text
1: alpha
2: beta
3: gamma
```

A file can be read in several ways:

- `file.read()` reads the remaining content into one string.
- `file.readline()` reads one line (including its ending `\n`, if present).
- `file.readlines()` builds a list of remaining lines.
- `for line in file` processes one line at a time without creating a separate list of every line.

Use `rstrip("\n")` if you only want to remove a line-ending newline. `strip()` also removes spaces and tabs, which may be meaningful data.

**Try it:** Replace the `for` loop with two calls to `readline()`. What happens to the third line?

## 5. Write and append text

`write()` puts text into a file and returns the number of characters written. It does **not** add a newline automatically.

```python
with open("demo_log.txt", "w", encoding="utf-8") as file:
    file.write("Session 1\n")

with open("demo_log.txt", "a", encoding="utf-8") as file:
    file.write("Session 2\n")

with open("demo_log.txt", "r", encoding="utf-8") as file:
    print(file.read(), end="")
```

**Expected output:**

```text
Session 1
Session 2
```

If the second block used `"w"` instead of `"a"`, it would replace the first line rather than extend the file. For a file that must not already exist, `"x"` is another option.

## 6. Handle file errors where they can occur

Missing files, invalid paths, and permission problems can raise exceptions. For simple I/O errors, `OSError` covers several common cases, including `FileNotFoundError` and `PermissionError`.

```python
def read_message(filename: str) -> str | None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except OSError as error:
        print(f"Could not read file: {error}")
        return None


message = read_message("does_not_exist_demo.txt")
if message is None:
    print("No message available")
```

Only catch errors you can handle meaningfully. Here, `None` signals that reading did not succeed. The function does **not** treat an empty file (`""`) as a failure.

File operations can fail during `open()`, `read()`, or `write()`. A `with` block ensures that an opened file is closed, but it does not make I/O errors disappear. Use a `try` block around the appropriate operation when you need to report or recover from a failure.

## 7. Standard input, output, and error

Python exposes three standard text streams through the `sys` module:

| Stream | What it is used for | Example |
| :--- | :--- | :--- |
| `sys.stdin` | Read input | `sys.stdin.readline()` |
| `sys.stdout` | Write normal output | `sys.stdout.write("OK\n")` |
| `sys.stderr` | Report errors | `sys.stderr.write("Error\n")` |

For example, save this as `stream_demo.py` and run `python3 stream_demo.py`:

```python
import sys


def main() -> None:
    sys.stdout.write("Enter a nickname: ")
    sys.stdout.flush()
    nickname = sys.stdin.readline().rstrip("\n")

    if not nickname:
        sys.stderr.write("Error: no nickname provided\n")
        return

    sys.stdout.write(f"Welcome, {nickname}!\n")


if __name__ == "__main__":
    main()
```

- `readline()` usually includes the newline from pressing Enter; at end-of-file, it returns an empty string.
- `stdout.write()` does not add `\n` automatically, unlike `print()`.
- `flush()` forces buffered text to be sent to the stream now, useful for a prompt without a newline.
- `stderr` is separate from regular output, so a shell can redirect the two streams independently.

You already know `input()`, which is convenient for simple interactive programs. Direct stream access is useful when you need more control over prompts and output.

## 8. Putting it together: a small command-line reader

This example combines `sys.argv`, a context manager, and error reporting. Save it as `view_text.py`:

```python
import sys


def main() -> None:
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 view_text.py FILE\n")
        return

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            print(file.read(), end="")
    except (OSError, UnicodeError) as error:
        sys.stderr.write(f"Cannot read text: {error}\n")


if __name__ == "__main__":
    main()
```

Run `python3 view_text.py demo_log.txt` after running the writing example in section 5. Then try a filename that does not exist and observe how the program responds.

## Common mistakes

| Mistake | Better approach |
| :--- | :--- |
| Opening an important file with `"w"` by accident | Check whether you need `"r"`, `"a"`, or `"x"` instead. |
| Leaving a file open | Use `with open(...)` or a `finally` block that calls `close()`. |
| Assuming a relative path starts beside the script | Check the current working directory. |
| Printing a file's text with an extra blank line | Consider `print(content, end="")`. |
| Removing meaningful spaces with `strip()` | Use `rstrip("\n")` when only the line ending should go. |
| Sending error messages to standard output | Use `sys.stderr` for diagnostics. |
| Treating a missing file as an empty file | Distinguish `None` or an exception from the empty string `""`. |

## Knowledge check

Before looking at the code again, explain:

1. What is the difference between `"r"`, `"w"`, and `"a"`? Which mode could accidentally delete existing content?
2. Why do we close files? How does `with` help even if an error occurs?
3. What is the difference between `read()`, `readline()`, and iterating over a file?
4. Why might `print(file.read())` add an unwanted blank line?
5. What changes when a program writes a message to `stderr` instead of `stdout`?
6. Why might an I/O operation raise `OSError`, and when should you catch it?

**Predict the final contents of the file:**

```python
with open("demo_prediction.txt", "w", encoding="utf-8") as file:
    file.write("A\n")
with open("demo_prediction.txt", "a", encoding="utf-8") as file:
    file.write("B\n")
with open("demo_prediction.txt", "w", encoding="utf-8") as file:
    file.write("C\n")
```

What would change if the last mode were `"a"`?

### Next step

Try modifying the examples and explaining each result without looking up the answer. In the next update, you will get original practice challenges and optional reference programs to explore after solving problems independently.

---

[← 03 — Data Structures](../03-data-structures/README.md) · [Chapter index](../README.md) · [05 — Advanced Object-Oriented Python →](../05-advanced-oop/README.md)
