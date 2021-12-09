import pytest

from .main import lanternfish_cycle

input_data = [3, 4, 3, 1, 2]


@pytest.fixture
def file_input_data():
    with open('2021/day_06/input.txt', 'r') as f:
        return [int(i) for i in f.read().split(',')]


@pytest.mark.parametrize('days, fishes', (
    (18, 26),
    (80, 5934),
    (256, 26984457539),
))
def test_lanternfish_cycle(days, fishes):
    assert lanternfish_cycle(input_data, days) == fishes


@pytest.mark.parametrize('days, fishes', (
    (80, 351092),
    (256, 1595330616005),
))
def test_lanternfish_cycle_from_file(file_input_data, days, fishes):
    assert lanternfish_cycle(file_input_data, days=days) == fishes
