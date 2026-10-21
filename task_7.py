from pathlib import Path


path = Path(input("Путь к каталогу: ").strip())
ext = input("Расширение: ").strip()

if not path.is_dir():
    print(f"Каталог не найден: {path}")
    quit()

ext = ext.lstrip("*")
if not ext.startswith("."):
    ext = "." + ext

all_items = list(path.rglob("*"))

files = [p for p in all_items if p.is_file()]
found = [p for p in files if p.suffix.lower() == ext.lower()]

print(f"\nНайдено файлов {ext} ({len(found)}):")
if found:
    for p in found:
        try:
            size = p.stat().st_size
        except OSError:
            size = -1
        print(f"  {p}  -  {size} байт")
else:
    print("  - не найдено")