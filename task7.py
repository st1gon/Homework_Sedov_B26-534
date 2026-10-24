from pathlib import Path

directory_name = input("Каталог: ")
file_extension = input("Расширение: ")
if not file_extension.startswith("."):
    file_extension = "." + file_extension

root_path = Path(directory_name).expanduser()

try:
    if not root_path.exists():
        raise FileNotFoundError(f"Каталог не существует: {root_path}")
    if not root_path.is_dir():
        raise NotADirectoryError(f"Это не каталог: {root_path}")
    has_matches = False
    for matched_file in root_path.rglob(f"*{file_extension}"):
        if matched_file.is_file():
            has_matches = True
            print(f"{matched_file} — {matched_file.stat().st_size} байт")
    if not has_matches:
        print("Файлы не найдены")
except (FileNotFoundError, NotADirectoryError) as error:
    print(f"Ошибка: {error}")
except PermissionError as error:
    print(f"Нет прав доступа: {error}")
