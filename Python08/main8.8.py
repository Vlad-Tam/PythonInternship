def sum_elements(arr):
    positive_sum = 0
    negative_sum = 0
    for num in arr:
        if num > 0:
            positive_sum += num
        else:
            negative_sum += num
    return positive_sum, negative_sum


def main():
    numbers = [5, -3, 8, -2, 1, -6, 4, -1, 3, -4]
    positive_sum, negative_sum = sum_elements(numbers)
    print(f"Positive sum: {positive_sum}")
    print(f"Negative sum: {negative_sum}")


if __name__ == "__main__":
    main()
