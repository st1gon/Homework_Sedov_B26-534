import re
from collections import Counter

log_pattern = re.compile(
    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (?P<level>INFO|WARNING|ERROR) User (?P<user>\d+)"
)

level_counts = Counter()
users_with_errors = set()

try:
    with open("app.log", "r", encoding="utf-8") as log_file:
        for log_line in log_file:
            match_result = log_pattern.match(log_line)
            if match_result:
                level_counts[match_result["level"]] += 1
                if match_result["level"] == "ERROR":
                    users_with_errors.add(match_result["user"])
except OSError as error:
    print(f"Ошибка чтения файла: {error}")
else:
    for severity in ("INFO", "WARNING", "ERROR"):
        print(f"{severity}: {level_counts[severity]}")
    print("Пользователи с ошибками:", ", ".join(sorted(users_with_errors, key=int)))
