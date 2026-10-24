import re

product_codes = ["PRD-12345", "PRD-00123", "USR-12345", "PRD-987", "PRD-ABCDE", "PRD-54321"]

matching_codes = [code for code in product_codes if re.fullmatch(r"PRD-\d{5}", code)]
print(matching_codes)
