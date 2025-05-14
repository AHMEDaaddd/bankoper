import logging
from logging import FileHandler, Formatter

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = Formatter("%(asctime)s [%(name)s] [%(levelname)s] %(message)s")
file_handler.setFormatter(file_formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    try:
        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.debug(f"Masked card number successfully: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Error in get_mask_card_number: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    try:
        masked = f"**{account_number[-4:]}"
        logger.debug(f"Masked account number successfully: {masked}")
        return masked

    except Exception as e:
        logger.error(f"Error in get_mask_account: {e}")
        raise
