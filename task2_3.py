def longest_series(sequence):
    """
    Находит самую длинную серию одинаковых элементов подряд.
    """
    if not sequence:
        return None, 0

    max_len = 1
    current_len = 1
    best_value = sequence[0]
    current_value = sequence[0]

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            current_len += 1
        else:
            current_len = 1
            current_value = sequence[i]

        if current_len > max_len:
            max_len = current_len
            best_value = current_value

    return best_value, max_len


if __name__ == "__main__":
    seq = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5, 5]
    val, length = longest_series(seq)
    print(f"Элемент: {val}, Длина серии: {length}")
