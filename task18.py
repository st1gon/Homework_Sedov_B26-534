import json
import logging
import re
from collections import Counter

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

LINE = re.compile(
    r"^\S+ \S+ (?P<ip>\d{1,3}(?:\.\d{1,3}){3}) (?P<method>[A-Z]+) (?P<url>\S+) (?P<code>\d{3})$"
)


def analyze(input_path, output_path):
    method_counts = Counter()
    url_counts = Counter()
    client_errors = 0

    try:
        with open(input_path, "r", encoding="utf-8") as source_file:
            logger.info("Начало обработки %s", input_path)
            for line_number, raw_line in enumerate(source_file, 1):
                match_result = LINE.match(raw_line.strip())
                if not match_result:
                    logger.warning("Строка %d не распознана", line_number)
                    continue
                method_counts[match_result["method"]] += 1
                url_counts[match_result["url"]] += 1
                if match_result["code"].startswith("4"):
                    client_errors += 1
    except FileNotFoundError:
        logger.error("Файл не найден: %s", input_path)
        return
    except PermissionError:
        logger.error("Нет прав доступа: %s", input_path)
        return
    except OSError as error:
        logger.error("Ошибка чтения файла: %s", error)
        return

    stats = {
        "requests_by_method": dict(method_counts),
        "errors_4xx": client_errors,
        "most_common_url": url_counts.most_common(1)[0][0] if url_counts else None,
    }
    with open(output_path, "w", encoding="utf-8") as source_file:
        json.dump(stats, source_file, ensure_ascii=False, indent=4)
    logger.info("Статистика сохранена в %s", output_path)


if __name__ == "__main__":
    analyze("access.log", "access_stats.json")
