import re
from collections import Counter

levels = Counter()
error_users = set()

with open(input("Путь к файлу логов: ").strip(), encoding='utf-8') as f:
    for line in f:
        m = re.search(r'\b(INFO|WARNING|ERROR)\b.*?User (\d+)', line)
        if m:
            level, user = m.groups()
            levels[level] += 1
            if level == 'ERROR':
                error_users.add(user)

print(f"INFO: {levels['INFO']}")
print(f"WARNING: {levels['WARNING']}")
print(f"ERROR: {levels['ERROR']}")

if error_users:
    print("\nПользователи с ошибками:", ", ".join(sorted(error_users, key=int)))
