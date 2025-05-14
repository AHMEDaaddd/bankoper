import os
from typing import Dict

import requests  # type: ignore


def convert_to_rub(transaction: Dict) -> float:
    """Конвертирует сумму в рубли, если валюта USD или EUR,
    иначе возвращает сумму как есть."""
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"from": currency, "to": "RUB", "amount": amount}
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return float(data.get("result", 0.0))

    raise ConnectionError(f"API request failed with status code {response.status_code}")
