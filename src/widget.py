"""Модуль для работы с визуальным отображением операций."""

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Определяет, карта это или счет, и маскирует соответственно."""
    if not data:
        return data
    if data.startswith("Счет") or data.lower().startswith("acc"):
        return f"Счет {get_mask_account(data.split()[-1])}"
    else:
        return get_mask_card_number("".join(filter(str.isdigit, data)))


def get_date(date_str: str) -> str:
    """Преобразует дату из строки в формат ДД.ММ.ГГГГ."""
    if not date_str:
        return date_str
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return date_str  # если дата некорректная, возвращаем как есть
