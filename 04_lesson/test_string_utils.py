# test_string_utils.py
import pytest
from string_utils import StringUtils


class TestStringUtils:

    # ===== Тесты для capitalize() =====
    @pytest.mark.positive
    def test_capitalize_regular_string(self):
        assert StringUtils.capitalize("тест") == "Тест"

    @pytest.mark.positive
    def test_capitalize_numeric_string(self):
        assert StringUtils.capitalize("123") == "123"

    @pytest.mark.positive
    def test_capitalize_string_with_spaces(self):
        assert StringUtils.capitalize("04 апреля 2023") == "04 апреля 2023"

    @pytest.mark.negative
    def test_capitalize_empty_string(self):
        assert StringUtils.capitalize("") == ""

    @pytest.mark.negative
    def test_capitalize_space_string(self):
        assert StringUtils.capitalize(" ") == " "

    @pytest.mark.negative
    def test_capitalize_none(self):
        with pytest.raises(AttributeError):
            StringUtils.capitalize(None)

    # ===== Тесты для trim() =====
    @pytest.mark.positive
    def test_trim_regular_string(self):
        assert StringUtils.trim("   тест") == "тест"

    @pytest.mark.positive
    def test_trim_mixed_spaces(self):
        assert StringUtils.trim(" \t\nтест") == "тест"

    @pytest.mark.negative
    def test_trim_empty_string(self):
        assert StringUtils.trim("") == ""

    @pytest.mark.negative
    def test_trim_space_string(self):
        assert StringUtils.trim(" ") == ""

    @pytest.mark.negative
    def test_trim_none(self):
        with pytest.raises(AttributeError):
            StringUtils.trim(None)

    # ===== Тесты для to_list() =====
    @pytest.mark.positive
    def test_to_list_regular_string(self):
        assert StringUtils.to_list("a,b,c") == ["a", "b", "c"]

    @pytest.mark.positive
    def test_to_list_with_spaces(self):
        assert StringUtils.to_list("1, 2, 3") == ["1", " 2", " 3"]

    @pytest.mark.negative
    def test_to_list_empty_string(self):
        assert StringUtils.to_list("") == [""]

    @pytest.mark.negative
    def test_to_list_space_string(self):
        assert StringUtils.to_list(" ") == [" "]

    @pytest.mark.negative
    def test_to_list_none(self):
        with pytest.raises(AttributeError):
            StringUtils.to_list(None)

    # ===== Тесты для contains() =====
    @pytest.mark.positive
    def test_contains_regular_string(self):
        assert StringUtils.contains("Тест", "е") is True

    @pytest.mark.positive
    def test_contains_numeric_string(self):
        assert StringUtils.contains("123", "2") is True

    @pytest.mark.negative
    def test_contains_empty_string(self):
        assert StringUtils.contains("", "x") is False

    @pytest.mark.negative
    def test_contains_space_string(self):
        assert StringUtils.contains(" ", "x") is False

    @pytest.mark.negative
    def test_contains_none(self):
        with pytest.raises(TypeError):
            StringUtils.contains(None, "е")
