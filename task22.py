import re

webpage_text = """Полезные сайты: https://python.org, http://example.com/page,
https://example.com/docs/index.html и ftp://files.example.com/data."""

for web_address in re.findall(r"https?://[^\s,]+?(?=[,.]?(?:\s|$))", webpage_text):
    print(web_address)
