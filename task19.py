import re

phone_text = """Звоните: +7 999 123-45-67, 8 999 123-45-67,
+7 (999) 123-45-67 или 8 (999) 123-45-67. Номер 12345 не телефон."""

phone_pattern = re.compile(r"(?:\+7|8) (?:\(\d{3}\)|\d{3}) \d{3}-\d{2}-\d{2}")

for phone_number in phone_pattern.findall(phone_text):
    print(phone_number)
