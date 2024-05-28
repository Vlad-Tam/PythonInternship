def count_numbers(numbers):
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    return count_dict


def main():
    numbers = [8, 1, 2, 3, 1, 2, 4, 2, 3, 5, 1, 9]
    result = count_numbers(numbers)
    print(result)


if __name__ == "__main__":
    main()
