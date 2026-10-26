def rotate_matrix_clockwise(matrix):
    """
    Поворот матрицы на 90 градусов по часовой стрелке.
    """
    if not matrix or not matrix[0]:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[rows - 1 - j][i] for j in range(rows)] for i in range(cols)]


def rotate_matrix_counter_clockwise(matrix):
    """
    Поворот матрицы на 90 градусов против часовой стрелки.
    """
    if not matrix or not matrix[0]:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[j][cols - 1 - i] for j in range(rows)] for i in range(cols)]


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6]]
    print("Исходная:")
    for row in mat:
        print(row)

    print("\nПо часовой стрелке:")
    for row in rotate_matrix_clockwise(mat):
        print(row)

    print("\nПротив часовой стрелки:")
    for row in rotate_matrix_counter_clockwise(mat):
        print(row)
