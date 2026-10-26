def top_three_chars(text):
    """
    Возвращает 3 наиболее частых символа (без пробелов, регистронезависимо).
    """
    freq = {}
    first_seen = {}

    for idx, char in enumerate(text.lower()):
        if char == " ":
            continue
        freq[char] = freq.get(char, 0) + 1
        if char not in first_seen:
            first_seen[char] = idx

    sorted_chars = sorted(freq.keys(), key=lambda c: (-freq[c], first_seen[c]))

    result = [(char, freq[char]) for char in sorted_chars[:3]]
    return result


if __name__ == "__main__":
    sample_text = "Hello World! Programming in Python is amazing."
    print("Топ-3 символа:", top_three_chars(sample_text))
