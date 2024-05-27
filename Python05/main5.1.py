import numpy as np


def main():
    n = int(input('Input matrix size: '))
    matrix = np.random.randint(1, 10, size=(n, n))
    print(matrix)


if __name__ == '__main__':
    main()
