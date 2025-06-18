"""Модуль генерации отчётов по транзакциям: по категориям, дням недели и типу дня."""

import logging

import pandas as pd

from src.utils.xlsx_reader import load_transactions

logger = logging.getLogger(__name__)


def spending_by_category(
    df: pd.DataFrame,
    category: str,
    date_time: str | None = None,
) -> pd.DataFrame:
    """Возвращает сумму трат по указанной категории."""
    logger.info("Генерация отчета: траты по категории")
    df = df[df["Категория"] == category]
    df = df[df["Сумма операции"] < 0]

    if date_time is not None:
        end_date = pd.to_datetime(date_time)
        start_date = end_date.replace(day=1, hour=0, minute=0, second=0)
        op_dates = pd.to_datetime(df["Дата операции"], dayfirst=True)
        df = df[(op_dates >= start_date) & (op_dates <= end_date)]

    result = df.groupby("Категория")["Сумма операции"].sum().sort_values()
    return result.to_frame(name="Сумма операции")


def spending_by_weekday() -> pd.DataFrame:
    """Возвращает сумму трат по дням недели из таблицы операций."""
    logger.info("Генерация отчета: траты по дням недели")
    df = load_transactions()
    df = df[df["Сумма операции"] < 0]
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    df["День недели"] = df["Дата операции"].dt.day_name()
    result = df.groupby("День недели")["Сумма операции"].sum().sort_values()
    return result.to_frame(name="Сумма операции")


def spending_by_workday() -> pd.DataFrame:
    """Возвращает сумму трат по рабочим и выходным дням."""
    logger.info("Генерация отчета: траты по рабочим/выходным дням")
    df = load_transactions()
    df = df[df["Сумма операции"] < 0]
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    df["Тип дня"] = df["Дата операции"].dt.weekday.apply(lambda x: "Рабочий" if x < 5 else "Выходной")
    result = df.groupby("Тип дня")["Сумма операции"].sum().sort_values()
    return result.to_frame(name="Сумма операции")
