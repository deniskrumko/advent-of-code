"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
import re

import pytest


def atoi(s: str, b: int = 2**31) -> int:
    match = re.search('^[-+]?[0-9]+', s.lstrip())
    value = int(match.group()) if match else 0
    return max(-b, value) if value < 0 else min(b - 1, value)


@pytest.mark.parametrize('value, expected', (
    ('42', 42),
    ('    -42 ', -42),
    ('1231 and words', 1231),
    ('3.14159', 3),
    ('  -0012a42', -12),
    ('words and 123', 0),
    ('+-12', 0),
    ('2147483648', 2147483647),
    ('-91283472332', -2147483648),
))
def test_atoi(value, expected):
    assert atoi(value) == expected
