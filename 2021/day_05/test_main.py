import pytest

from .main import find_intersections_on_map

input_data = '''
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''.strip().split('\n')


@pytest.fixture
def file_input_data():
    with open('2021/day_05/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


@pytest.mark.parametrize('use_diagonals, expected', (
    (False, 5),
    (True, 12),
))
def test_find_intersections_on_map(use_diagonals, expected):
    assert find_intersections_on_map(input_data, use_diagonals) == expected


@pytest.mark.parametrize('use_diagonals, expected', (
    (False, 3990),
    (True, 21305),
))
def test_find_intersections_on_map_from_file(file_input_data, use_diagonals, expected):
    assert find_intersections_on_map(file_input_data, use_diagonals) == expected
