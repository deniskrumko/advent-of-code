import pytest

from .main import (
    INPUT_FILE,
    Puzzle,
    function_1,
    function_2,
)

input_data = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip('\n')

input_data_north = """
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
""".strip('\n')

input_data_cycle_1 = """
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
""".strip('\n')

input_data_cycle_2 = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O
""".strip('\n')

input_data_cycle_3 = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
""".strip('\n')


@pytest.fixture
def file_input_data():
    with open(INPUT_FILE, 'r') as f:
        return f.read()


# TESTS

def test_function_1():
    assert function_1(input_data) == 136


def test_function_1_from_file(file_input_data):
    assert function_1(file_input_data) == 110565


def test_function_2():
    assert function_2(input_data) == 64


def test_function_2_from_file(file_input_data):
    assert function_2(file_input_data) == 89845


def test_tilt():
    p = Puzzle(input_data)
    expected = Puzzle(input_data_north)
    assert (p.tilt_north().df == expected.df).all().all()


@pytest.mark.parametrize('cycles, expected', (
    (1, input_data_cycle_1),
    (2, input_data_cycle_2),
    (3, input_data_cycle_3),
))
def test_cycle_tilt(cycles, expected):
    p = Puzzle(input_data)
    expected = Puzzle(expected)
    assert (p.cycle_tilt(cycles).df == expected.df).all().all()
