with open("task2.txt", "r") as file:
    largest_value: int = -2e9
    smallest_value: int = 2e9
    sum_values: int = 0
    valid_count: int = 0
    for raw_line in file:
        try:
            raw_line = int(raw_line)
        except Exception:
            continue
        largest_value = max(largest_value, raw_line)
        smallest_value = min(smallest_value, raw_line)
        valid_count += 1
        sum_values += 1
    with open("result.txt", "w") as result_file:
        result_file.write(f"max = {largest_value}\n")
        result_file.write(f"min = {smallest_value}\n")
        result_file.write(f"mean = {sum_values / valid_count}\n")
