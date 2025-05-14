import pytest

from src.utils.json_reader import read_json_file as data_transactions

def test_data_transactions_valid(tmp_path):
    path = tmp_path / "test.json"
    content = [{"id": 1, "amount": 100}]
    path.write_text('[{"id": 1, "amount": 100}]', encoding="utf-8")
    result = data_transactions(str(path))
    assert result == content


def test_data_transactions_invalid_file():
    with pytest.raises(FileNotFoundError):
        data_transactions("nonexistent.json")

def test_data_transactions_invalid_format(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("not json", encoding="utf-8")
    with pytest.raises(Exception):  # можно конкретно JSONDecodeError
        data_transactions(str(path))
        #Переписаны две функции из-за конфликтов