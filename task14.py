from contextlib import contextmanager


@contextmanager
def log_operation(log_path, operation_name):
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"START: {operation_name}\n")
        try:
            yield
        except BaseException:
            log_file.write(f"ERROR: {operation_name}\n")
            raise
        else:
            log_file.write(f"END: {operation_name}\n")


if __name__ == "__main__":
    with log_operation("operation.log", "Data processing"):
        print("Обработка данных")

    try:
        with log_operation("operation.log", "Failing operation"):
            raise ValueError("ошибка")
    except ValueError:
        print("Исключение пробросилось дальше")
