sum_values = 0
numbers_count = 0
min_value = None
max_value = None

try:
    with open("big_numbers.txt", "r") as file:
        for raw_line in file:
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            try:
                number = int(raw_line)
            except ValueError:
                continue
            sum_values += number
            numbers_count += 1
            min_value = number if min_value is None else min(min_value, number)
            max_value = number if max_value is None else max(max_value, number)
except OSError as error:
    print(f"Ошибка чтения файла: {error}")
else:
    if numbers_count:
        print(f"Сумма: {sum_values}")
        print(f"Минимум: {min_value}")
        print(f"Максимум: {max_value}")
        print(f"Количество: {numbers_count}")
        print(f"Среднее: {sum_values / numbers_count}")
    else:
        print("Нет чисел в файле")
