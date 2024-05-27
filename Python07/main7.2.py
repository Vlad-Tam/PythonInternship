def create_matrix() -> list[list[int]]:
    rows = int(input("Input matrix rows amount: "))
    cols = int(input("Input matrix columns amount: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            elem = int(input(f"Input value [{i}][{j}]: "))
            row.append(elem)
        matrix.append(row)
    return matrix


def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print(row)


def sum_matrix(matrix: list[list[int]]) -> None:
    total = 0
    for row in matrix:
        total += sum(row)
    return total


def max_matrix(matrix: list[list[int]]) -> int:
    max_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_elem:
                max_elem = elem
    return max_elem


def min_matrix(matrix: list[list[int]]) -> int:
    min_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_elem:
                min_elem = elem
    return min_elem


def main():
    matrix = create_matrix()
    print("Your matrix:")
    print_matrix(matrix)
    print(f"Sum of elements: {sum_matrix(matrix)}")
    print(f"Max element: {max_matrix(matrix)}")
    print(f"Min element: {min_matrix(matrix)}")


if __name__ == '__main__':
    main()
