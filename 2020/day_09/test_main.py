from .main import (
    get_encryption_weakness,
    get_incorrect_value,
)

input_data = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


def test_get_incorrect_value():
    assert get_incorrect_value(input_data, preamble=5) == 127


def test_get_encryption_weakness():
    assert get_encryption_weakness(input_data, preamble=5) == 62


def test_2020_day_09_input():
    with open('2020/day_09/input.txt', 'r') as f:
        input_data = f.read()
        assert get_incorrect_value(input_data) == 14360655
        assert get_encryption_weakness(input_data) == 1962331
