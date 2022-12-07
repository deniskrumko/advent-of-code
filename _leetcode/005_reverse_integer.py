"""
https://leetcode.com/problems/reverse-integer/
"""
import pytest


def reverse(x: int, b: int = 2**31) -> int:
    z = int(str(x)[::-1].strip('-')) * (-1 if x < 0 else 1)
    return z if -b < z < b else 0


@pytest.mark.parametrize('value, expected', (
    (123, 321),
    (-1000, -1),
    (120, 21),
    (123123123123, 0),
    (-123123123123, 0),
))
def test_reverse(value, expected):
    assert reverse(value) == expected
