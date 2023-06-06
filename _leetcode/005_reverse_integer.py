"""
https://leetcode.com/problems/reverse-integer/
"""
import pytest

from . import measure_execution_speed


def my_reverse(x: int, b: int = 2**31) -> int:
    z = int(str(x)[::-1].strip('-')) * (-1 if x < 0 else 1)
    return z if -b < z < b else 0


def chatgpt_reverse(x):
    return (
        0 if abs(x) > 2**31
        else int(str(x)[::-1]) if x >= 0 else -int(str(abs(x))[::-1])
    )


@pytest.mark.parametrize('value, expected', (
    (123, 321),
    (-1000, -1),
    (120, 21),
    (123123123123, 0),
    (-123123123123, 0),
))
def test_reverse(value, expected):
    assert my_reverse(value) == chatgpt_reverse(value) == expected


def test_speed_of_reverse():
    measure_execution_speed(my_reverse, chatgpt_reverse, x=123456789)
