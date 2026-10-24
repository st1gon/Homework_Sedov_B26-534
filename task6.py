from pathlib import Path

root_path = Path(input("Путь к каталогу: ")).expanduser()

if not root_path.is_dir():
    print("Каталог не найден")
else:
    all_files = [entry for entry in root_path.rglob("*") if entry.is_file()]
    subdirectories = [entry for entry in root_path.rglob("*") if entry.is_dir()]
    python_files = [entry for entry in all_files if entry.suffix == ".py"]
    bytes_total = sum(entry.stat().st_size for entry in all_files)

    print(f"Файлов: {len(all_files)}")
    print(f"Подкаталогов: {len(subdirectories)}")
    print("Python-файлы:")
    for entry in python_files:
        print(f"  {entry}")
    print(f"Суммарный размер: {bytes_total} байт")
