import pytest

from .main import (
    get_answers_set,
    get_sum_of_answers,
)

input_data = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def test_get_sum_of_answers():
    assert get_sum_of_answers(input_data, unique=True) == 11
    assert get_sum_of_answers(input_data, unique=False) == 6


@pytest.mark.parametrize('value, unique, same', (
    (['ab', 'ac'], {'a', 'b', 'c'}, {'a'}),
    (['abc'], {'a', 'b', 'c'}, {'a', 'b', 'c'}),
    (['a', 'a'], {'a'}, {'a'}),
    (['b'], {'b'}, {'b'}),
    (['a', 'b', 'c'], {'a', 'b', 'c'}, set()),
))
def test_get_unique_or_same_answers(value, unique, same):
    assert get_answers_set(value, unique=True) == unique
    assert get_answers_set(value, unique=False) == same


def test_2020_day_06_input():
    with open('2020/day_06/input.txt', 'r') as f:
        input_data = f.read()
        assert get_sum_of_answers(input_data, unique=True) == 6683
        assert get_sum_of_answers(input_data, unique=False) == 3122
