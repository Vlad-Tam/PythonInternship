def calculate_sum(*args):
    total = 0
    for arg in args:
        total += (arg ** (1 / 2) + arg) / 2
    return total


def main():
    print(calculate_sum(5, 12, 19))
    print(calculate_sum(1, 2))


if __name__ == "__main__":
    main()
