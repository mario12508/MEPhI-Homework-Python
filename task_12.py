import re


with open(input("Путь к файлу с текстом: ").strip(), encoding='utf-8') as f:
    text = f.read()

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
unique_emails = list(dict.fromkeys(emails))

print("Результат:")
for email in unique_emails:
    print(email)
