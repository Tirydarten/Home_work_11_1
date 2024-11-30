from typing import Any, Dict, Generator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
    """Генератор для фильтрации транзакций по валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """Генератор для получения описаний транзакций."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        # Форматируем номер карты с ведущими нулями
        formatted_number = f"{number:016d}"  # Преобразуем в строку с 16 цифрами
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"


# Пример данных транзакций
transactions: List[Dict[str, Any]] = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

# Пример использования функций
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

descriptions = transaction_descriptions(transactions)

for _ in range(5):
    print(next(descriptions))


for card_number in card_number_generator(1, 5):
    print(card_number)
