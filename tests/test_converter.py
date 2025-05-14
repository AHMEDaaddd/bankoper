from unittest.mock import patch

import pytest

from src.external_api.converter import convert_to_rub


@patch("src.external_api.converter.requests.get")
def test_convert_to_rub_usd(mock_get, monkeypatch):
    monkeypatch.setenv("API_KEY", "test_key")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7400.0}

    transaction = {"amount": 100.0, "currency": "USD"}
    result = convert_to_rub(transaction)
    assert result == 7400.0


def test_convert_to_rub_rub():
    transaction = {"amount": 500.0, "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 500.0
