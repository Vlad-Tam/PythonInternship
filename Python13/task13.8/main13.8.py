from matrix import Matrix


def main() -> None:
    matrix1 = Matrix(3, 4, 1, 100)
    print("Matrix 1:")
    print(matrix1)
    print()

    matrix2 = Matrix()
    print("Matrix 2:")
    print(matrix2)
    print()

    print("Max element in matrix 1:", matrix1.find_max())
    print("Min element in matrix 1:", matrix1.find_min())
    print("Sum of elements in matrix 1:", matrix1.sum_all())


if __name__ == "__main__":
    main()
