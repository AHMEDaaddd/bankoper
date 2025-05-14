"""Модуль с генераторами: filter_by_currency, transaction_descriptions.

card_number_generator.

"""

from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """Фильтрует транзакции по коду валюты.

    :param transactions: Список транзакций.
    :param currency_code: Код валюты (например, "USD").
    :return: Итератор отфильтрованных транзакций.

    """
    for tx in transactions:
        if (
            tx.get("operationAmount", {}).get("currency", {}).get("code")
            == currency_code
        ):
            yield tx


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """Возвращает описания транзакций.

    :param transactions: Список транзакций.
    :return: Итератор описаний транзакций.

    """
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение (включительно).
    :param stop: Конечное значение (включительно).
    :return: Итератор номеров карт.

    """
    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[
            4:8
        ] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:]
