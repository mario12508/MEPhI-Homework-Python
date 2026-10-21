import re
import json
import logging
from collections import Counter
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def process_logs(filepath):
    path = Path(filepath)

    if not path.is_file():
        logging.error(f"Файл не найден: {path}")
        return

    pattern = re.compile(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([A-Z]+)\s+(\S+)\s+(\d{3})')

    methods = Counter()
    urls = Counter()
    errors_4xx = 0

    logging.info(f"Начало обработки файла: {path}")

    try:
        with path.open(encoding='utf-8') as f:
            for line in f:
                m = pattern.search(line)
                if m:
                    ip, method, url, status = m.groups()
                    status = int(status)

                    methods[method] += 1
                    urls[url] += 1

                    if 400 <= status < 500:
                        errors_4xx += 1
                else:
                    logging.warning(
                        f"Не удалось распарсить строку: {line.strip()}")

    except PermissionError:
        logging.error(f"Нет прав на чтение файла: {path}")
        return
    except OSError as e:
        logging.error(f"Ошибка ОС при чтении файла: {e}")
        return

    logging.info("Обработка завершена")

    most_frequent_url = urls.most_common(1)[0][0] if urls else None

    stats = {
        "methods": dict(methods),
        "errors_4xx": errors_4xx,
        "most_frequent_url": most_frequent_url
    }

    out_path = Path("stats.json")
    try:
        with out_path.open('w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=4)
        logging.info(f"Статистика сохранена в {out_path}")
    except OSError as e:
        logging.error(f"Ошибка при сохранении JSON: {e}")

    return stats
