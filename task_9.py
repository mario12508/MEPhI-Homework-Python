import re


def parse_number(value):
    if not isinstance(value, str):
        raise ValueError(f"Ожидалась строка, получено: {type(value).__name__}")

    s = value.strip()
    if not re.fullmatch(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?', s):
        raise ValueError(f"Некорректное значение: {value!r}")

    return float(s)


while True:
    raw = input("Введите число (или 'q' для выхода): ").strip()
    if raw.lower() == 'q':
        break
    try:
        num = parse_number(raw)
    except ValueError as e:
        print(f"Ошибка: {e}")
        continue
    print(f"Число: {num}")
