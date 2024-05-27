def sum_and_max(*args) -> int:
    result = 0
    max_value = args[0]
    for el in args:
        result += el
        if el > max_value:
            max_value = el
    return result, max_value


if __name__ == "__main__":
    print(sum_and_max(4, 3, 23, 1))
    print(sum_and_max(112, 22, 3, 43, 5))
