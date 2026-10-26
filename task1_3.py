def create_chess_matrix(n, m, first_val=0, symbols=None):
    """
    Создает матрицу n x m в шахматном порядке.
    """
    if symbols is not None and len(symbols) == 2:
        val1, val2 = symbols
    else:
        val1, val2 = first_val, 1 if first_val == 0 else 0

    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            current = val1 if (i + j) % 2 == 0 else val2
            row.append(current)
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    print("Матрица 3x5 с 0 и 1:")
    for r in create_chess_matrix(3, 5, first_val=0):
        print(r)

    print("\nПрямоугольная матрица 2x4 с символами '#' и '.':")
    for r in create_chess_matrix(2, 4, symbols=("#", ".")):
        print(r)
