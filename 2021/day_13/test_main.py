import pytest

from .main import (
    make_all_folds,
    make_one_fold_and_count,
)

input_data = '''
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''.strip().split('\n')

input_expected_map = '''
#####
#...#
#...#
#...#
#####
.....
.....
'''.strip().split('\n')

file_expected_map = '''
..##.####..##..#..#..##..###..###..###.
...#....#.#..#.#..#.#..#.#..#.#..#.#..#
...#...#..#....#..#.#..#.#..#.#..#.###.
...#..#...#.##.#..#.####.###..###..#..#
#..#.#....#..#.#..#.#..#.#....#.#..#..#
.##..####..###..##..#..#.#....#..#.###.
'''.strip().split('\n')


@pytest.fixture
def file_input_data():
    with open('2021/day_13/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def test_make_one_fold_and_count(file_input_data):
    assert make_one_fold_and_count(input_data) == 17
    assert make_one_fold_and_count(file_input_data) == 942


def prepare_expected_from_map(expected_map):
    expected = {}
    for i in range(len(expected_map)):
        for j in range(len(expected_map[0])):
            if expected_map[i][j] == '#':
                expected[(i, j)] = '#'

    return expected


def test_make_all_folds():
    expected = prepare_expected_from_map(input_expected_map)
    assert make_all_folds(input_data) == expected


def test_make_all_folds_from_file(file_input_data):
    expected = prepare_expected_from_map(file_expected_map)
    assert make_all_folds(file_input_data) == expected
