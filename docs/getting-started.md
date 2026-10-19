# Getting Started

[← Home](../README.md) · [Learning path](learning-path.md) · [Chapter index](../modules/README.md)

Welcome! This guide helps you **learn the tools, understand Python code, and practice independently** before tackling larger projects. You do not need previous Python experience to begin.

**In 15–20 minutes, you will:** check your Python installation, open the repository, run a small program, change its behavior, and learn a repeatable study routine.

> This is an independent learning resource, not official 42 material. The examples and challenges are original.

## 1. What you need

- **Python 3:** A maintained Python 3 release is recommended (Python 3.11+ is a reasonable starting point). If your campus or project specifies a version, follow that requirement.
- **A terminal:** Terminal on Linux/macOS or PowerShell on Windows.
- **A code editor:** VS Code, Vim, or any editor you are comfortable with.
- **Git (recommended):** Useful for keeping your local copy up to date; alternatively, download the repository as a ZIP from GitHub.

You do **not** need external Python libraries to run today's example.

### Check Python

**Linux and macOS:**

```bash
python3 --version
```

**Windows (PowerShell):**

```powershell
py --version
```

If `py` is not available, try `python --version`. You should see something like `Python 3.x.y`.

If Python is missing, install it from [python.org/downloads](https://www.python.org/downloads/) and reopen the terminal before checking again. On Ubuntu/Debian, you can also install Python using your distribution's package manager, e.g. `sudo apt install python3 python3-venv` (after updating package indexes). **Do not replace or remove the Python installation used by your operating system.**

## 2. Get the repository

On its GitHub page, choose **Code → Download ZIP**, extract it, and open the extracted folder in your terminal. If you use Git, choose **Code → HTTPS** and copy the clone URL, then run `git clone` with that URL.

For example, after downloading or cloning:

```bash
cd 42-python-learning-path
```

Make sure you are in the **repository root**, the folder containing `README.md`, `docs/`, `modules/` and `examples/`. The commands below assume you are there.

If the extracted ZIP folder has a slightly different name, use that name in the `cd` command.

## 3. Run your first Python program

Open [`examples/first_steps.py`](../examples/first_steps.py). It uses a function, a list, a loop, and a formatted string. You do not need to understand every line yet.

**Linux and macOS:**

```bash
python3 examples/first_steps.py
```

**Windows (PowerShell):**

```powershell
py examples/first_steps.py
```

If your Windows installation uses `python` instead of `py`, run `python examples/first_steps.py`.

Expected output:

```text
Hello, Ada!
Hello, Grace!
Hello, Guido!
Total learners: 3
```

You have just executed a `.py` file. Python reads the file and runs the statements inside it.

### What happened?

| Code | Idea |
| :--- | :--- |
| `learners = [...]` | Store several values in a list. |
| `def greet(name: str) -> str:` | Define a function; the annotations describe intended types. |
| `for learner in learners:` | Repeat work for each item. |
| `print(...)` | Send text to standard output. |
| `f"Hello, {name}!"` | Insert a value into a formatted string. |
| `if __name__ == "__main__":` | Call `main()` when this file is run directly. |

Type annotations communicate intent; **they do not automatically enforce types at runtime**. We will explore them more deeply later.

## 4. Try it yourself (no solution provided)

Before changing the file, **predict** what will happen. Then edit, save, and rerun it.

1. Add a fourth learner to the list. What changes in the output?
2. Change the greeting so it uses the learner's name in uppercase. Look up the string method `upper()` if needed.
3. Make the program print how many names contain at least five characters. Try a loop and an `if` condition.

These are independent warm-up challenges, not assignments from a 42 project. Keep your own solutions in a separate working copy if you want to compare approaches.

## 5. An optional virtual environment

A virtual environment keeps third-party packages for one project separate from those used by other projects. **You can skip this for today's example**, which uses only Python's standard features. It will be useful when later chapters introduce dependencies.

From the repository root, create and activate one:

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python examples/first_steps.py
deactivate
```

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python examples/first_steps.py
deactivate
```

If PowerShell blocks script activation, you can still run the environment's interpreter without changing system execution policies:

```powershell
.\.venv\Scripts\python.exe examples/first_steps.py
```

The `.venv/` folder is already excluded by this repository's `.gitignore`. **Never commit virtual environments, installed dependencies, or secrets.**

## 6. Learn effectively with this repository

Follow this routine for each chapter:

1. **Read:** Understand the goal and learn the vocabulary in the chapter outline.
2. **Predict:** Before executing an example, guess what it will print or return.
3. **Run:** Execute it yourself; do not just read it.
4. **Modify:** Change an input, a condition, or the program structure.
5. **Debug:** Treat exceptions and unexpected output as clues.
6. **Explain:** Describe *why* the program works in your own words.
7. **Practice:** Solve original challenges without looking at reference code first.

When a chapter is labeled **Outline**, its full lessons and practice activities are still being developed. See the [learning path](learning-path.md) for the current sequence.

## 7. Common problems

| Problem | What to check |
| :--- | :--- |
| `python3: command not found` or `py` unavailable | Confirm installation; try the OS-specific command above. |
| `can't open file ...` | Check that the terminal is in the repository root and the file exists under `examples/`. |
| `SyntaxError` after an edit | Check quotes, parentheses, colons and indentation. |
| `IndentationError` | Use consistent indentation (four spaces per level is conventional). |
| `ModuleNotFoundError` | Check the module name and which Python interpreter you are running; do not install packages blindly. |
| Terminal shows old output | Save the file and rerun it; check you edited the same file you executed. |
| `venv` cannot be created on Ubuntu/Debian | Check whether the `python3-venv` OS package is installed. |

A useful first debugging habit is to **read the last line of a traceback**, then follow the indicated file and line number.

## 8. What's next?

- Continue to [Chapter 00 — Python Fundamentals](../modules/00-fundamentals/README.md).
- Explore the [full learning path](learning-path.md).
- If you want additional official reference material, use the [Python Tutorial](https://docs.python.org/3/tutorial/) and the [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

---

[← Home](../README.md) · [Learning path →](learning-path.md)
