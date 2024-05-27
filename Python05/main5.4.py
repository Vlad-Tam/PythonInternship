import numpy as np


def generate_matrix():
    n = int(input('Input matrix rows amount: '))
    m = int(input('Input matrix columns amount: '))
    return np.random.randint(1, 10, size=(n, m))


def find_values_count(matr) -> int:
    count = 0
    mean = np.mean(matr)
    print(f'Mean value is: {mean}')

    for i in range(matr.shape[0]):
        for j in range(matr.shape[1]):
            if ((i + j) % 2 == 0) & (matr[i, j] > mean):
                count += 1
    return count


if __name__ == '__main__':
    matrix = generate_matrix()
    print(matrix)
    print(f'Amount of elements: {find_values_count(matrix)}')
