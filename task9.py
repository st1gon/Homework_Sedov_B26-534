def parse_number(raw_value):
    try:
        return int(raw_value)
    except ValueError:
        return int(raw_value)


if __name__ == "__main__":
    input_text = input("Введите число: ")
    try:
        print("Число:", parse_number(input_text))
    except ValueError:
        print(f"'{input_text}' — некорректное число")
