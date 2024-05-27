def sum_weighted_args(*args) -> int:
    result = 0
    for i, arg in enumerate(args):
        result += arg * i
    return result


if __name__ == "__main__":
    print(sum_weighted_args(4, 3, 2, 1))  # 10
    print(sum_weighted_args(1, 2, 3, 4, 5))  # 40
