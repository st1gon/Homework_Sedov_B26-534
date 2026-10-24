import re

log_text = """INFO User 123 logged in
ERROR User 456 authentication failed
WARNING User 123 changed password
ERROR User 789 authentication failed
INFO User 456 logged in"""


found_user_ids = re.findall(r"User (\d+)", log_text)
failed_lines = re.findall(r"^ERROR.*$", log_text, re.MULTILINE)
users_with_errors = re.findall(r"^ERROR User (\d+)", log_text, re.MULTILINE)

print("Пользователи:", found_user_ids)
print("Строки ERROR:", failed_lines)
print("Пользователи с ошибками:", users_with_errors)
