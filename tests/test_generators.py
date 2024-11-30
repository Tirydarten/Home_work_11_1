from typing import Dict, List

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_usd_transactions(setup: List[Dict]) -> None:
    """Тестирование фильтрации транзакций в USD"""
    filtered_transactions: List[Dict] = list(filter_by_currency(setup, "USD"))
    assert len(filtered_transactions) == 3  # Ожидаем три транзакции в USD


def test_filter_rub_transactions(setup: List[Dict]) -> None:
    """Тестирование фильтрации транзакций в RUB"""
    filtered_transactions: List[Dict] = list(filter_by_currency(setup, "RUB"))
    assert len(filtered_transactions) == 2  # Ожидаем две транзакции в RUB


def test_no_matching_currency(setup: List[Dict]) -> None:
    """Тестирование случая, когда нет транзакций в заданной валюте"""
    filtered_transactions: List[Dict] = list(filter_by_currency(setup, "EUR"))
    assert len(filtered_transactions) == 0  # Ожидаем ноль транзакций в EUR


def test_empty_transaction_list(setup: List[Dict]) -> None:
    """Тестирование обработки пустого списка транзакций"""
    filtered_transactions: List[Dict] = list(filter_by_currency([], "USD"))
    assert len(filtered_transactions) == 0  # Ожидаем ноль транзакций


def test_no_currency_operations() -> None:
    """Тестирование обработки списка без операций в заданной валюте"""
    transactions_without_usd: List[Dict] = [
        {"id": 1, "operationAmount": {"amount": "1000", "currency": {"code": "EUR"}}},
        {"id": 2, "operationAmount": {"amount": "2000", "currency": {"code": "EUR"}}},
    ]
    filtered_transactions: List[Dict] = list(filter_by_currency(transactions_without_usd, "USD"))
    assert len(filtered_transactions) == 0  # Ожидаем ноль транзакций


def test_transaction_descriptions(setup: List[Dict]) -> List[str]:
    """Тестирование получения описаний транзакций"""
    descriptions: List[str] = list(transaction_descriptions(setup))
    expected_descriptions: List[str] = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert descriptions == expected_descriptions
    return descriptions


def test_empty_transaction_descriptions_list(setup: List[Dict]) -> List[str]:
    """Тестирование обработки пустого списка транзакций"""
    descriptions: List[str] = list(transaction_descriptions([]))
    assert descriptions == []  # Ожидаем пустой список
    return descriptions


def test_single_transaction() -> str:
    """Тестирование получения описания для одной транзакции"""
    single_transaction: Dict = {
        "id": 1,
        "operationAmount": {"amount": "1000", "currency": {"code": "EUR"}},
        "description": "Тестовая транзакция",
    }
    descriptions: List[str] = list(transaction_descriptions([single_transaction]))
    assert descriptions == ["Тестовая транзакция"]  # Ожидаем одно описание
    return descriptions[0]


def test_card_number_formatting() -> None:
    """Тестирование корректности форматирования номеров карт."""
    generated_numbers: List[str] = list(card_number_generator(0, 5))
    expected_numbers: List[str] = [
        "0000 0000 0000 0000",
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert generated_numbers == expected_numbers


def test_card_number_range() -> None:
    """Тестирование генерации номеров в заданном диапазоне."""
    generated_numbers: List[str] = list(card_number_generator(100, 105))
    expected_numbers: List[str] = [
        "0000 0000 0000 0100",
        "0000 0000 0000 0101",
        "0000 0000 0000 0102",
        "0000 0000 0000 0103",
        "0000 0000 0000 0104",
        "0000 0000 0000 0105",
    ]
    assert generated_numbers == expected_numbers


def test_edge_case() -> None:
    """Тестирование крайних значений диапазона."""
    start_value: int = int("9999000000000000")
    end_value: int = int("9999000000000011")

    generated_numbers: List[str] = list(card_number_generator(start_value, end_value))

    assert len(generated_numbers) > 0  # "Генератор должен вернуть хотя бы один номер."

    expected_start: str = "9999 0000 0000 0000"
    assert generated_numbers[0] == expected_start  # Проверяем первый номер

    expected_end: str = "9999 0000 0000 0011"  # Это будет последним номером
    assert generated_numbers[-1] == expected_end  # Проверяем последний номер
