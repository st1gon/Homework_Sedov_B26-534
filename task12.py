import re

contact_text = """Контакты:
alice@example.com
bob@test.org
alice@example.com
admin@company.ru"""

email_addresses = re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", contact_text)

for address in dict.fromkeys(email_addresses):
    print(address)
