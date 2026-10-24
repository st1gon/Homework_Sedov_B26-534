import re

meeting_text = """Встречи состоятся 15.09.2026, 21.09.2026 и 03.10.2026.
Следующая встреча запланирована на 1.11.2026."""

# формат DD.MM.YYYY — ровно две цифры дня и месяца, поэтому 1.11.2026 не подходит
for meeting_date in re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", meeting_text):
    print(meeting_date)
