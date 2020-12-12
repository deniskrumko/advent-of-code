import pytest

from .main import (
    count_solutions,
    count_solutions_by_recursive,
    get_1_and_3_differences,
    get_differences,
)

input_data = """
16
10
15
5
1
11
7
19
6
12
4
"""

input_data_2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


@pytest.mark.parametrize('value, expected', (
    (input_data, {1: 7, 3: 5}),
    (input_data_2, {1: 22, 3: 10}),
))
def test_get_differences(value, expected):
    assert get_differences(value) == expected


@pytest.mark.parametrize('value, expected', (
    (input_data, 8),
    (input_data_2, 19208),
))
def test_count_solutions_by_recursive(value, expected):
    assert count_solutions_by_recursive(value) == expected


@pytest.mark.parametrize('value, expected', (
    (input_data, 8),
    (input_data_2, 19208),
))
def test_ccount_solutions_by_logic(value, expected):
    assert count_solutions(value) == expected


def test_2020_day_10_input():
    with open('2020/day_10/input.txt', 'r') as f:
        input_data = f.read()
        assert get_1_and_3_differences(input_data) == 3034
        assert count_solutions(input_data) == 259172170858496
