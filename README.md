
# 💼 Bank Operations Project with Logging

## 📦 Структура

- `src/masks.py` — маскировка данных + логирование
- `src/utils/json_reader.py` — чтение JSON-файлов + логирование
- `logs/` — сюда пишутся логи
- `run_logs_test.py` — скрипт для проверки логирования

---

## ⚙️ Установка

1. Установите зависимости:
```bash
poetry install
```

2. Проверьте типы:
```bash
poetry run mypy src
```

3. Проверьте оформление кода:
```bash
poetry run flake8 src
```

---

## 🚀 Тест логирования

1. Запустите тестовый скрипт:
```bash
poetry run python run_logs_test.py
```

2. Проверьте файлы логов:

- `logs/masks.log` — события из `masks.py`
- `logs/utils.log` — события из `json_reader.py`

---

## 📄 Пример логов

```
2025-05-14 18:30:02 [masks] [DEBUG] Masked card number successfully: 1234 56** **** 5678
2025-05-14 18:30:02 [utils] [DEBUG] Successfully read JSON file: data/operations.json
```

---

## 🧪 Примечание

Если файл `data/operations.json` не найден, будет предпринята попытка загрузки из `data/data/operations.json`.
