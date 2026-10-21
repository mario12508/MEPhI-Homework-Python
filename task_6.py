from pathlib import Path


path = Path(input("Путь к каталогу: ").strip())

if not path.is_dir():
    print(f"Каталог не найден: {path}")
    quit()

all_items = list(path.rglob("*"))

files = [p for p in all_items if p.is_file()]
dirs = [p for p in all_items if p.is_dir()]
py_files = [p for p in files if p.suffix == ".py"]

total_size = 0
for p in files:
    try:
        total_size += p.stat().st_size
    except OSError:
        pass

print(f"Файлов: {len(files)}")
print(f"Подкаталогов: {len(dirs)}")
print(f"Суммарный размер: {total_size} байт")

print(f"\nФайлы .py ({len(py_files)}):")
if py_files:
    for f in py_files:
        print(f"  {f}")
else:
    print("  - не найдено")
