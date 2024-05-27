import random


def create_random_matrix(n, random_from=1, random_to=9):
    matrix = []
    for i in range(n):
        row = [random.randint(random_from, random_to) for i in range(n)]
        matrix.append(row)
    return matrix


def main():
    size = int(input("Enter the matrix size: "))
    min_value = int(input("Enter the minimum value (default is 1): ") or 1)
    max_value = int(input("Enter the maximum value (default is 9): ") or 9)

    random_matrix = create_random_matrix(size, random_from=min_value, random_to=max_value)
    print("Generated matrix:")
    for row in random_matrix:
        print(row)


if __name__ == '__main__':
    main()
