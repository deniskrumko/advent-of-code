"""
https://leetcode.com/problems/zigzag-conversion/

For N = 4:

P     I     N
 A   L S   I G
  Y A   H R
   P     I
"""
import pytest

from . import measure_execution_speed


def get_indexes(num: int, max_index: int):
    """Find indexes for traversing strings as zigzag."""
    mod = (num * 2 - 2) or 1
    top_indexes = [i for i in range(max_index + num) if i % mod == 0]
    yield from (t for t in top_indexes if 0 <= t < max_index)

    for i in range(1, num):
        results = set()
        for top_index in top_indexes:
            results.update({top_index - i, top_index + i})

        yield from sorted(v for v in results if 0 <= v < max_index)


def zigzag_conversion(value: str, num: int) -> str:
    """Get zigzag traversed string."""
    return ''.join(value[i] for i in get_indexes(num, len(value)))


def chatgpt_zigzag_conversion(value, num):
    if num == 1 or num >= len(value):
        return value

    result = [''] * num
    index = 0
    step = 1

    for char in value:
        result[index] += char

        if index == 0:
            step = 1
        elif index == num - 1:
            step = -1

        index += step

    return ''.join(result)


@pytest.mark.parametrize('value, num, expected', (
    ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
    ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
    ('A', 1, 'A'),
    ('ABC', 1, 'ABC'),
    ('ABCD', 3, 'ABDC'),
))
def test_zigzag_conversion(value, num, expected):
    assert zigzag_conversion(value, num) == chatgpt_zigzag_conversion(value, num) == expected


def test_speed_of_zigzag_conversion():
    measure_execution_speed(
        zigzag_conversion,
        chatgpt_zigzag_conversion,
        value='PAYPALISHIRING',
        num=3,
    )
