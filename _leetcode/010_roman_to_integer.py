"""
https://leetcode.com/problems/roman-to-integer/
"""
import pytest

# If you saw "009_integer_to_roman" then best solution is to precalculate all choices
int_to_roman_map = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}
roman_to_int_map = {v: k for k, v in int_to_roman_map.items()}


def roman_to_int(value: str) -> int:
    """Convert roman to int."""
    if value in roman_to_int_map:
        return roman_to_int_map[value]

    i = 2 if value[:2] in roman_to_int_map else 1
    return roman_to_int(value[:i]) + roman_to_int(value[i:])


@pytest.mark.parametrize('value, expected', (
    (3, 'III'),
    (4, 'IV'),
    (9, 'IX'),
    (80, 'LXXX'),
    (1258, 'MCCLVIII'),
    (1994, 'MCMXCIV'),
))
def test_roman_to_int(value, expected):
    assert roman_to_int(expected) == value
