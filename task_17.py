from pathlib import Path

path = Path(input("Путь к файлу: ").strip())

if not path.is_file():
    print(f"Файл не найден: {path}")
    quit()

total_sum = 0
count = 0
min_val = None
max_val = None

with path.open(encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            num = int(line)
        except ValueError:
            print(f"Пропущена некорректная строка: {line!r}")
            continue

        total_sum += num
        count += 1

        if min_val is None or num < min_val:
            min_val = num
        if max_val is None or num > max_val:
            max_val = num

if count == 0:
    print("Файл пуст или не содержит чисел")
else:
    print(f"Сумма: {total_sum}")
    print(f"Минимум: {min_val}")
    print(f"Максимум: {max_val}")
    print(f"Количество чисел: {count}")
    print(f"Среднее: {total_sum / count}")
