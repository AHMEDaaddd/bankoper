"""Модуль с функциями обработки операций и транзакций."""

from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]], status: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """Фильтрует список операций по заданному статусу."""
    return [op for op in operations if op.get("status") == status]


def sort_by_date(
    operations: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """Сортирует список операций по дате."""
    return sorted(
        operations, key=lambda op: datetime.fromisoformat(op["date"]), reverse=reverse
    )
