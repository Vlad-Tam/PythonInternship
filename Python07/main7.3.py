def factorial(n: int) -> int:
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    num = int(input("Input number: "))
    result = factorial(num)
    if result == -1:
        print("Factorial is undefined for n < 0")
    else:
        print(f"Factorial of {num} is: {result}")


if __name__ == '__main__':
    main()
