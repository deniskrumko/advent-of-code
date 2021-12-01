from .main import (
    get_stabilized_model,
    get_stabilized_model_count,
)

input_data = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

expected_data = """
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
"""


def test_get_stabilized_model():
    assert get_stabilized_model(input_data) == expected_data.split()


def test_get_stabilized_model_count():
    assert get_stabilized_model_count(input_data) == 37


def test_2020_day_11_input():
    with open('2020/day_11/input.txt', 'r') as f:
        input_data = f.read()
        assert get_stabilized_model_count(input_data) == 2346
