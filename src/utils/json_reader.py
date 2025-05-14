import json
import logging
from logging import FileHandler, Formatter
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = Formatter("%(asctime)s [%(name)s] [%(levelname)s] %(message)s")
file_handler.setFormatter(file_formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)


def read_json_file(path: str) -> Any:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logger.debug(f"Successfully read JSON file: {path}")
            return data
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"JSON decoding failed for {path}: {e}")
        raise
