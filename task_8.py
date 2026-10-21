from pathlib import Path


def read_file(path):
    p = Path(path)
    if not p.exists():
        print(f"Ошибка: файл не найден — {p}")
        return None

    if not p.is_file():
        print(f"Ошибка: это не файл — {p}")
        return None

    try:
        return p.read_text(encoding="utf-8")

    except PermissionError:
        print(f"Ошибка: нет прав на чтение файла — {p}")
    except FileNotFoundError:
        print(f"Ошибка: файл исчез до чтения — {p}")
    except IsADirectoryError:
        print(f"Ошибка: ожидался файл, получен каталог — {p}")
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось декодировать файл как UTF-8 — {p}")
    except OSError as e:
        print(f"Ошибка ОС при чтении файла {p}: {e}")

    return None
