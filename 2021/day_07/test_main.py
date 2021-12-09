import pytest

from .main import (
    find_min_fuel_consumption,
    fuel_consumption,
    fuel_consumption_2,
)

input_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


@pytest.fixture
def file_input_data():
    with open('2021/day_07/input.txt', 'r') as f:
        return [int(i) for i in f.read().split(',')]


@pytest.mark.parametrize('position, consumed_fuel', (
    (2, 37),
    (1, 41),
    (3, 39),
    (10, 71),
))
def test_fuel_consumption(position, consumed_fuel):
    assert fuel_consumption(input_data, position) == consumed_fuel


def test_fuel_consumption_2():
    assert fuel_consumption_2(input_data, 5) == 168


def test_find_min_fuel_consumption():
    assert find_min_fuel_consumption(input_data, 1) == 37


@pytest.mark.parametrize('variant, consumed_fuel', (
    (1, 352997),
    (2, 101571302),
))
def test_find_min_fuel_consumption_from_file(file_input_data, variant, consumed_fuel):
    assert find_min_fuel_consumption(file_input_data, variant) == consumed_fuel
