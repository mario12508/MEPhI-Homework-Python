import re

text = input("Введите текст: ")

pattern = r'(?:\+7|8)\s*(?:\(\d{3}\)|\d{3})\s*\d{3}-\d{2}-\d{2}'
phones = re.findall(pattern, text)

print("Найденные номера:")
for phone in phones:
    print(phone)
