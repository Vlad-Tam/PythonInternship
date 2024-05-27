import numpy as np


def generate_matrix():
    n = int(input('Input matrix rows amount: '))
    m = int(input('Input matrix columns amount: '))
    return np.random.randint(1, 10, size=(n, m))


def find_values_count(matr) -> int:
    count = 0
    for row in matr:
        for el in row:
            if el == 7:
                count += 1
    return count


if __name__ == '__main__':
    matrix = generate_matrix()
    print(matrix)
    print(f'Amount of numbers 7 in the matrix: {find_values_count(matrix)}')