from src.masks import get_mask_card_number, get_mask_account
from src.utils.json_reader import read_json_file

print(get_mask_card_number("1234567812345678"))
print(get_mask_account("40817810099910001234"))

# Попытка загрузить JSON-файл (сначала обычный путь, потом вложенный, если не найдёт)
try:
    read_json_file("data/operations.json")
except FileNotFoundError:
    read_json_file("data/data/operations.json")