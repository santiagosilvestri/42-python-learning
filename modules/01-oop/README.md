# 01 — Object-Oriented Programming

> **Status: In progress.** The concepts and runnable examples are available. Original practice challenges and optional reference code will follow in the next update.

[← Chapter index](../README.md) · [Learning path](../../docs/learning-path.md) · [Getting started](../../docs/getting-started.md) · [← 00 — Python Fundamentals](../00-fundamentals/README.md)

**Goal:** Learn how to organize data and behavior into objects, keep their state consistent, and reuse behavior without copying code. Allow about **25–35 minutes** to read and experiment with this lesson.

Before starting, make sure you understand [functions, loops, and types](../00-fundamentals/README.md).

## 1. Classes and objects

A **class** describes what a type of object knows (its *attributes*) and can do (its *methods*). An **instance** is a particular object created from that class.

```python
class StudySession:
    def __init__(self, topic: str, minutes: int) -> None:
        self.topic = topic
        self.minutes = minutes

    def describe(self) -> str:
        return f"{self.topic}: {self.minutes} minutes"


python = StudySession("Python", 40)
math = StudySession("Math", 25)

print(python.describe())  # Python: 40 minutes
print(math.describe())    # Math: 25 minutes
```

- `class` defines a new class.
- `__init__` initializes the instance after it is created.
- `self` refers to the current instance. Python supplies it when you call `python.describe()`.
- `self.topic` and `self.minutes` belong to that particular instance.

**Try it:** Change only `math.minutes`. Does `python.minutes` also change? Why not?

## 2. Instance state and methods

An instance method can **read or change an object's state**. This is useful when an action should update the data belonging to the same object.

```python
class Progress:
    def __init__(self, completed: int = 0) -> None:
        self.completed = completed

    def finish_task(self) -> None:
        self.completed += 1


progress = Progress()
progress.finish_task()
progress.finish_task()
print(progress.completed)  # 2
```

`finish_task()` changes the object; it does not need to return the new value. A method that *queries* state might return a value instead. Choose based on what the caller needs.

## 3. Instance attributes vs. class attributes

**Instance attributes** can differ for each object. **Class attributes** belong to the class and can provide shared defaults or constants.

```python
class Badge:
    category = "Learning"  # Class attribute

    def __init__(self, name: str) -> None:
        self.name = name   # Instance attribute


first = Badge("Loops")
second = Badge("Functions")
print(first.category, first.name)   # Learning Loops
print(second.category, second.name) # Learning Functions
```

Avoid using a mutable class attribute, such as a list, to store data that each instance should own. Put that list in `__init__` instead.

## 4. Encapsulation: protecting valid state

**Encapsulation** means exposing useful operations while controlling how an object's data changes. In Python, an underscore prefix (for example, `_points`) signals an attribute intended for internal use; it **does not** make the attribute truly private.

```python
class Score:
    def __init__(self) -> None:
        self._points = 0

    def add(self, amount: int) -> bool:
        if amount < 0:
            return False
        self._points += amount
        return True

    def get_points(self) -> int:
        return self._points


score = Score()
print(score.add(10))   # True
print(score.add(-3))   # False
print(score.get_points())  # 10
```

Here, callers should use `add()` rather than change `_points` directly. Other designs can use `@property`, but a method is often the simplest starting point.

## 5. Inheritance and `super()`

A **subclass** can reuse behavior from a **base class** and add its own features. `super()` lets the subclass call a method from the parent class's method resolution order.

```python
class Message:
    def __init__(self, text: str) -> None:
        self.text = text

    def display(self) -> str:
        return self.text


class UrgentMessage(Message):
    def __init__(self, text: str, priority: int) -> None:
        super().__init__(text)
        self.priority = priority

    def display(self) -> str:
        return f"[P{self.priority}] {super().display()}"


message = UrgentMessage("Save your work", 1)
print(message.display())  # [P1] Save your work
```

`UrgentMessage` **inherits** from `Message`. Its `display()` method **overrides** the inherited method, while `super().display()` reuses the parent behavior. Use inheritance when the relationship is genuinely an *is-a* relationship.

## 6. Polymorphism: one interface, different behavior

Different objects can respond to the **same method call** in different ways. This is one of the benefits of polymorphism.

```python
class PlainReport:
    def render(self) -> str:
        return "Tasks completed: 3"


class DetailedReport:
    def render(self) -> str:
        return "Tasks completed: 3; remaining: 2"


reports = [PlainReport(), DetailedReport()]
for report in reports:
    print(report.render())
```

These two classes do not even need a shared base class for this example: both provide `render()`. Python can use common behavior without requiring inheritance. You'll explore this idea further with [protocols and duck typing in Chapter 05](../05-advanced-oop/README.md).

## 7. Three kinds of methods

An ordinary **instance method** receives `self`. A **class method** receives `cls` and is useful for alternative constructors. A **static method** receives neither automatically and can hold a related utility.

```python
class StudyPlan:
    def __init__(self, minutes: int) -> None:
        self.minutes = minutes

    @classmethod
    def from_hours(cls, hours: int) -> "StudyPlan":
        return cls(hours * 60)

    @staticmethod
    def is_long_session(minutes: int) -> bool:
        return minutes >= 60

    def describe(self) -> str:
        return f"Plan: {self.minutes} minutes"


plan = StudyPlan.from_hours(2)
print(plan.describe())                   # Plan: 120 minutes
print(StudyPlan.is_long_session(120))   # True
```

`cls` refers to the class being called, so `from_hours()` creates an instance of that class. A static method is not required for ordinary helper functions; use one only when the function logically belongs with the class.

## 8. Composition and nested classes

**Composition** means one object contains or uses other objects: a library *has books*, rather than *is a book*. It is often simpler than inheritance when you want to combine features.

```python
class Book:
    def __init__(self, title: str) -> None:
        self.title = title


class Shelf:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)


shelf = Shelf()
shelf.add_book(Book("Python Basics"))
print(shelf.books[0].title)  # Python Basics
```

A class may also be **nested** inside another class to group closely related definitions. Nesting does not automatically connect instances of those classes or give the inner class access to an outer instance. Usually, start with ordinary classes unless nesting improves clarity.

## Common mistakes to watch for

| Mistake | Better approach |
| :--- | :--- |
| Forgetting `self` in an instance method | Declare it as the first parameter of an instance method. |
| Writing `topic = topic` inside `__init__` | Use `self.topic = topic` to store instance state. |
| Sharing one list across every instance accidentally | Create the list inside `__init__`. |
| Assuming `_value` is inaccessible from outside | Treat `_` as a naming convention, not access control. |
| Overriding `__init__` without initializing needed parent state | Call `super().__init__(...)` where appropriate. |
| Adding inheritance just to reuse a small amount of code | Consider composition or a helper function. |
| Expecting type annotations to enforce types automatically | Validate inputs when runtime safety is required. |

## Check your understanding

Try to explain these without looking back at the examples:

1. What is the difference between a class and an instance?
2. What does `self` refer to when two different instances call the same method?
3. Why might changing a mutable class attribute cause surprising behavior?
4. What is the difference between *overriding* a method and *calling it with* `super()`?
5. When would you choose composition instead of inheritance?
6. How do `self`, `cls`, and static methods differ?

**Predict the output:**

```python
class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increase(self) -> None:
        self.value += 1


a = Counter()
b = Counter()
a.increase()
a.increase()
b.increase()
print(a.value, b.value)
```

**Next update:** original OOP exercises, a debugging challenge, and optional code examples to inspect after you practice independently.

---

[← 00 — Python Fundamentals](../00-fundamentals/README.md) · [Chapter index](../README.md) · [02 — Error Handling →](../02-error-handling/README.md)
