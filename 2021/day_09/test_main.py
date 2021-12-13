import pytest

from .main import (
    find_basins,
    get_sum_of_lowest_points,
)


@pytest.fixture
def input_data():
    test_map = '''
    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    '''
    rows = test_map.strip().split('\n')
    return [[j for j in i.strip()] for i in rows]


@pytest.fixture
def file_input_data():
    with open('2021/day_09/input.txt', 'r') as f:
        return [[i for i in line.strip()] for line in f.readlines()]


def test_get_sum_of_lowest_points(input_data):
    assert get_sum_of_lowest_points(input_data) == 15


def test_get_sum_of_lowest_points_from_file(file_input_data):
    assert get_sum_of_lowest_points(file_input_data) == 480


def test_find_basins(input_data):
    assert find_basins(input_data) == 1134


def test_find_basins_from_file(file_input_data):
    assert find_basins(file_input_data) == 1045660
