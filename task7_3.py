def find_most_similar_strings(strings):
    """
    Находит пару строк одинаковой длины с минимальным количеством различий.
    """
    by_length = {}
    for s in strings:
        by_length.setdefault(len(s), []).append(s)

    min_diffs = float("inf")
    best_pair = (None, None)
    found = False

    for length, group in by_length.items():
        if len(group) < 2:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                s1, s2 = group[i], group[j]
                diffs = sum(1 for c1, c2 in zip(s1, s2) if c1 != c2)
                if diffs < min_diffs:
                    min_diffs = diffs
                    best_pair = (s1, s2)
                    found = True

    if not found:
        return None, None, -1
    return best_pair[0], best_pair[1], min_diffs


if __name__ == "__main__":
    lst = ["abcdef", "abcxef", "xyz123", "abcdeg", "hello"]
    s1, s2, diff = find_most_similar_strings(lst)
    print(f"Строки: '{s1}' и '{s2}', различий: {diff}")
