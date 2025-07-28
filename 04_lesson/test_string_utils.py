import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Тесты для capitalize()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),          # обычная строка
    ("hello world", "Hello world"),  # строка с пробелом
    ("python", "Python"),          # одно слово
    ("Тест", "Тест"),              # кириллица (уже с заглавной)
    ("123", "123"),                # числа как строка
    ("04 апреля 2023", "04 апреля 2023")  # строка с пробелами и числами
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                      # пустая строка
    (" ", " "),                    # строка с пробелом
    ("123abc", "123abc"),          # начинается с цифры
    ("   ", "   "),                # только пробелы
    (None, None),                  # None (ожидаем ошибку)
    ([], [])                       # пустой список (ожидаем ошибку)
])
def test_capitalize_negative(input_str, expected):
    if input_str is None or isinstance(input_str, list):
        with pytest.raises((AttributeError, TypeError)):
            string_utils.capitalize(input_str)
    else:
        assert string_utils.capitalize(input_str) == expected


# Тесты для trim()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),        # пробелы слева
    ("  Тест", "Тест"),            # кириллица
    ("  123", "123"),              # числа
    ("  04 апреля 2023", "04 апреля 2023"),  # строка с пробелами
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                      # пустая строка
    (" ", ""),                     # строка с пробелом
    ("test  ", "test  "),          # пробелы справа
    (None, None),                  # None (ожидаем ошибку)
    ([], [])                       # пустой список (ожидаем ошибку)
])
def test_trim_negative(input_str, expected):
    if input_str is None or isinstance(input_str, list):
        with pytest.raises((AttributeError, TypeError)):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected


# Тесты для contains()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),         # обычный случай
    ("Тест", "е", True),           # кириллица
    ("123", "2", True),            # числа
    ("04 апреля 2023", "апреля", True),  # подстрока с пробелами
    ("hello world", " ", True)     # пробел как символ
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "a", False),              # пустая строка
    (" ", "a", False),             # строка с пробелом
    ("SkyPro", "U", False),        # нет символа
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("invalid_input, symbol", [
    (None, "a"),
    ([], "a"),
    (123, "a")
])
def test_contains_invalid_input(invalid_input, symbol):
    with pytest.raises((AttributeError, TypeError)):
        string_utils.contains(invalid_input, symbol)


# Тесты для delete_symbol()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),      # обычный случай
    ("Тест", "е", "Тст"),          # кириллица
    ("12345", "34", "125"),        # числа
    ("04 апреля 2023", " ", "04апреля2023"),  # удаление пробелов
    ("hello world", "o", "hell wrld")  # несколько вхождений
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "a", ""),                 # пустая строка
    (" ", "a", " "),               # строка с пробелом
    ("SkyPro", "X", "SkyPro"),     # нет символа
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("invalid_input, symbol", [
    (None, "a"),
    ([], "a"),
    (123, "a"),
    ({}, "a")
])
def test_delete_symbol_invalid_input(invalid_input, symbol):
    """Проверяем обработку невалидных входных данных"""
    with pytest.raises((AttributeError, TypeError)):
        string_utils.delete_symbol(invalid_input, symbol)
