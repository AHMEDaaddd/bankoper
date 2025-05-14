import json

from typing import Any, List


def data_transactions(filepath: str) -> List[dict]:
    """Считывает JSON-файл и возвращает список транзакций."""
    try:
        with open(filepath, encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []
