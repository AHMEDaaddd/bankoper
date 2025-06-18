from unittest.mock import patch

import pandas as pd

from src.reports import spending_by_category, spending_by_weekday, spending_by_workday


def test_spending_by_category(sample_df):
    result = spending_by_category(sample_df, "Кафе")
    assert isinstance(result, pd.DataFrame)
    assert not result.empty


@patch("src.utils.xlsx_reader.load_transactions")
def test_spending_by_weekday(mock_get_df, sample_df):
    mock_get_df.return_value = sample_df.to_dict(orient="records")
    result = spending_by_weekday()
    assert isinstance(result, pd.DataFrame)
    assert result["Сумма операции"].sum() < 0


@patch("src.utils.xlsx_reader.load_transactions")
def test_spending_by_workday(mock_get_df, sample_df):
    mock_get_df.return_value = sample_df.to_dict(orient="records")
    result = spending_by_workday()
    assert "Рабочий" in result.index or "Выходной" in result.index
    assert result["Сумма операции"].sum() < 0
