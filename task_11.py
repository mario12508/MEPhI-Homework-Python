import re

with open(input("Путь к файлу логов: ").strip(), encoding='utf-8') as f:
    lines = f.readlines()

users = re.findall(r'User (\d+)', ''.join(lines))
unique_users = sorted(set(users), key=int)

errors = [line.rstrip('\n') for line in lines if re.search(r'\bERROR\b', line)]

error_users = sorted(set(re.findall(r'ERROR User (\d+)', ''.join(errors))), key=int)

print("Все идентификаторы пользователей:", unique_users)
print("\nСтроки с ERROR:")
for line in errors:
    print(f"  {line}")
print("\nПользователи с ошибкой:", error_users)
