import numpy as np


def generate_matrix():
    n = int(input('Input matrix size: '))
    return np.random.randint(1, 10, size=(n, n))


def calculate_summary(matr) -> int:
    summary = 0
    for row in matr:
        for el in row:
            if el % 3 == 0:
                summary += el
    return summary


if __name__ == '__main__':
    matrix = generate_matrix()
    print(matrix)
    print(f'Sum of multiples of three: {calculate_summary(matrix)}')
