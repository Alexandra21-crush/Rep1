import pytest
from string_utils import StringUtils

class TestStringUtils:
    utils = StringUtils()

    # Тесты для capitalize()
    def test_capitalize_regular_string(self):
        assert self.utils.capitalize("skypro") == "Skypro"
    
    def test_capitalize_already_capitalized(self):
        assert self.utils.capitalize("Skypro") == "Skypro"
    
    def test_capitalize_empty_string(self):
        assert self.utils.capitalize("") == ""
    
    def test_capitalize_single_character(self):
        assert self.utils.capitalize("s") == "S"
    
    def test_capitalize_with_spaces(self):
        assert self.utils.capitalize(" skypro") == " skypro"

    # Тесты для trim()
    def test_trim_leading_spaces(self):
        assert self.utils.trim("   skypro") == "skypro"
    
    def test_trim_no_leading_spaces(self):
        assert self.utils.trim("skypro") == "skypro"
    
    def test_trim_empty_string(self):
        assert self.utils.trim("") == ""
    
    def test_trim_only_spaces(self):
        assert self.utils.trim("    ") == ""
    
    def test_trim_mixed_spaces(self):
        assert self.utils.trim("  s k y p r o  ") == "s k y p r o  "

    # Тесты для contains()
    def test_contains_present_symbol(self):
        assert self.utils.contains("SkyPro", "S") is True
    
    def test_contains_missing_symbol(self):
        assert self.utils.contains("SkyPro", "U") is False
    
    def test_contains_empty_string(self):
        assert self.utils.contains("", "S") is False
    
    def test_contains_empty_symbol(self):
        assert self.utils.contains("SkyPro", "") is True
    
    def test_contains_case_sensitive(self):
        assert self.utils.contains("SkyPro", "s") is False

    # Тесты для delete_symbol()
    def test_delete_symbol_single_char(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"
    
    def test_delete_symbol_multiple_chars(self):
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"
    
    def test_delete_symbol_not_found(self):
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"
    
    def test_delete_symbol_all_occurrences(self):
        assert self.utils.delete_symbol("abababa", "a") == "bbb"
    
    def test_delete_symbol_empty_string(self):
        assert self.utils.delete_symbol("", "a") == ""
    
    def test_delete_symbol_empty_symbol(self):
        assert self.utils.delete_symbol("SkyPro", "") == "SkyPro"

    # Дополнительные тесты для edge cases
    def test_capitalize_special_chars(self):
        assert self.utils.capitalize("123abc") == "123abc"
        assert self.utils.capitalize("été") == "Été"
    
    def test_trim_non_space_whitespace(self):
        assert self.utils.trim("\t\nskypro") == "\t\nskypro"
    
    def test_contains_unicode_symbols(self):
        assert self.utils.contains("Привет", "иве") is True
        assert self.utils.contains("😊🌍", "🌍") is True
