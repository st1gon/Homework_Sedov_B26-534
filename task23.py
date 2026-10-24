import re

source_text = "Это   строка    с     большим    количеством   пробелов."
print(re.sub(r" {2,}", " ", source_text))

padded_text = "   Текст   с   пробелами   "
print(repr(re.sub(r" {2,}", " ", padded_text).strip()))
# то же без strip(): re.sub(r"^ +| +$", "", ...)
