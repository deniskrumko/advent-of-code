"""
https://leetcode.com/problems/integer-to-roman/
"""
import math

import pytest

symbol_to_value = '''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''

symbol_to_value_map = dict(
    line.split()
    for line in symbol_to_value.strip().splitlines()[1:]
)
value_to_symbol_map = {int(v): k for k, v in symbol_to_value_map.items()}


def convert_part_to_roman(value: int) -> str:
    """Small helper func :)"""
    if value == 0:
        return ''

    if value in value_to_symbol_map:
        return value_to_symbol_map[value]

    nearest10 = 10 ** math.floor(math.log10(value))
    nearest50 = nearest10 * 5

    if value == nearest10 * 4:
        return convert_part_to_roman(nearest10) + convert_part_to_roman(nearest50)
    elif value == nearest10 * 9:
        return convert_part_to_roman(nearest10) + convert_part_to_roman(nearest10 * 10)
    elif value > nearest50:
        return convert_part_to_roman(nearest50) + convert_part_to_roman(value - nearest50)
    else:
        multiplier = value // nearest10
        return value_to_symbol_map[nearest10] * multiplier


def convert_int_to_roman(value: int) -> str:
    """My solution to convert int to roman."""
    return ''.join(
        convert_part_to_roman(value=part * (10 ** (len(str(value)) - i - 1)))
        for i, part in enumerate(int(v) for v in str(value))
    )


def best_int_to_roman(num: int):
    """Best solution (not mine). Very clean and fast.

    https://leetcode.com/problems/integer-to-roman/solutions/462641/python-pythonic-simple-solution-88-9-100-0/
    """
    roman = {
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
    romanized = ''

    for base, symb in roman.items():
        romanized += symb * (num // base)
        num %= base
    else:
        return romanized


@pytest.mark.parametrize('value, expected', (
    (3, 'III'),
    (4, 'IV'),
    (9, 'IX'),
    (80, 'LXXX'),
    (1258, 'MCCLVIII'),
    (1994, 'MCMXCIV'),
))
def test_convert_int_to_roman(value, expected):
    assert convert_int_to_roman(value) == expected
