import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [("skypro", "Skypro"), ("hello world", "Hello world"), ("python", "Python")])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [("       banana", "banana"), ("   ", ""), ("My name is Marina", "My name is Marina")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, res,", [('Sun', 'S', True), ('123456', '5', True), ('Moon', 'K', False)])
def test_contains_positive(input_str, symbol, res):
    assert string_utils.contains(input_str, symbol) == res


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [(None), (123), (["skypro"])])
def test_trim_invalid_types(invalid_input):
    assert string_utils.trim(invalid_input)  
    
    with pytest.raises(AttributeError):
        string_utils.trim(invalid_input)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [("123abc", "123abc"), ("", ""), ("   ", "   ")])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, res", [("SkyPro", "U", False), ("SkyPro", "s", False), ("SkyPro", "", True)])
def test_contains_negative(input_str, symbol, res):
    assert string_utils.contains(input_str, symbol) == res


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [("SkyPro", "z", "SkyPro"), ("SkyPro", "K", "SkyPro"), ("SkyPro", "", "SkyPro")])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [("SkyPro", "k", "SyPro"), ("SkyPro", "Sky", "Pro"), ("banana", "a", "bnn")])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
    