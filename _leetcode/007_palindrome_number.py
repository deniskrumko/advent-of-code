"""
https://leetcode.com/problems/palindrome-number/

Solution 1: Pure maths without strings
Solution 2: Simple string solution
"""
import math
import time

import pytest


def get_palindrome_using_math(number: int, x: int = 0) -> int:
    if number < 10:
        return number

    result, remainder = divmod(number, 10)
    x = x or 10 ** math.floor(math.log10(number))
    return remainder * x + get_palindrome_using_math(result, x // 10)


def get_palindrome_using_str(number: int) -> int:
    return int(str(number)[::-1]) if number > 10 else number


def number_is_palindrome(number: int) -> bool:
    return number == get_palindrome_using_math(number) if number > 9 else number >= 0


@pytest.mark.parametrize('value, palindrome, expected', (
    (123, 321, False),
    (1000, 1, False),
    (12345, 54321, False),
    (1, 1, True),
    (0, 0, True),
    (121, 121, True),
    (1234567654321, 1234567654321, True),
))
def test_number_is_palindrome(value, palindrome, expected):
    assert get_palindrome_using_math(value) == get_palindrome_using_str(value) == palindrome
    assert number_is_palindrome(value) == expected


@pytest.mark.parametrize('value', (
    4294967296,
    123,
    1,
    1231231283912039109,
    381029381092380192830182309123,
    1000000000000000000000000000000000000,
))
def test_speed_get_palindrome(value):
    time_start = time.time()
    a = get_palindrome_using_math(value)
    time_end = time.time()
    print(f'\n  - Solution 1 (math): {(time_end - time_start) * 1000:.9f} ms')

    time_start = time.time()
    b = get_palindrome_using_str(value)
    time_end = time.time()
    print(f'  - Solution 2 (str):  {(time_end - time_start) * 1000:.9f} ms')

    assert a == b
