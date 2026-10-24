def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as source_file:
            return source_file.read()
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except PermissionError:
        print(f"Нет прав доступа к файлу: {file_path}")
    except IsADirectoryError:
        print(f"Это каталог, а не файл: {file_path}")
    except UnicodeDecodeError:
        print(f"Невозможно прочитать файл (неверная кодировка): {file_path}")
    except OSError as error:
        print(f"Ошибка операционной системы: {error}")
    return None


if __name__ == "__main__":
    file_content = read_file(input("Путь к файлу: "))
    if file_content is not None:
        print(file_content)
