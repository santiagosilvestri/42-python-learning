"""A tiny, original example to explore basic Python syntax."""


def greet(name: str) -> str:
    """Return a friendly message for one learner."""
    return f"Hello, {name}!"


def main() -> None:
    learners = ["Ada", "Grace", "Guido"]

    for learner in learners:
        print(greet(learner))

    print(f"Total learners: {len(learners)}")


if __name__ == "__main__":
    main()
