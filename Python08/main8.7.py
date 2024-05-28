def is_power_n(k, n):
    if k <= 0 or n <= 1:
        return False

    while k % n == 0:
        k //= n

    return k == 1


def main():
    n = 3
    numbers = [11, 5, 4, 8, 16, 32, 3, 128, 9, 512, 27, 64]
    count = 0
    for num in numbers:
        if is_power_n(num, n):
            count += 1
    print(f"Count of degrees of {n} in list: {count}")


if __name__ == "__main__":
    main()
