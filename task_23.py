import re

text1 = "Это   строка    с     большим    количеством   пробелов."
text2 = "   Текст   с   пробелами   "

print(re.sub(r'\s+', ' ', text1))
print(re.sub(r'\s+', ' ', text2).strip())
