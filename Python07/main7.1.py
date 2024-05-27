names = ["Alice", "Bob", "Charlie", "David", "Eve"]


def greet(name: str) -> None:
    print(f"Hello, {name}")


if __name__ == '__main__':
    for name in names:
        greet(name)
