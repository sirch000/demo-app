"""Entry point for the hello application."""


def greet(name: str = "World") -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def main() -> None:
    """Run the hello application."""
    print(greet())


if __name__ == "__main__":
    main()
