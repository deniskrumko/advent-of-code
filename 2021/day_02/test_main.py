import pytest

from .main import (
    sumbarine_path,
    sumbarine_path_with_aim,
)

input_data = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]


@pytest.fixture
def file_input_data():
    with open('2021/day_02/input.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def test_sumbarine_path():
    assert sumbarine_path(input_data) == 150


def test_sumbarine_path_from_file(file_input_data):
    assert sumbarine_path(file_input_data) == 1488669


def test_sumbarine_path_with_aim():
    assert sumbarine_path_with_aim(input_data) == 900


def test_sumbarine_path_with_aim_from_file(file_input_data):
    assert sumbarine_path_with_aim(file_input_data) == 1176514794
