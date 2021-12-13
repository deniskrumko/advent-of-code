import pytest

from .main import (
    count_flashes_per_step,
    find_all_flashed_simultaneously,
    simulate_step,
)

steps = [
    '''
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
    ''',
    '''
    6594254334
    3856965822
    6375667284
    7252447257
    7468496589
    5278635756
    3287952832
    7993992245
    5957959665
    6394862637
    ''',
    '''
    8807476555
    5089087054
    8597889608
    8485769600
    8700908800
    6600088989
    6800005943
    0000007456
    9000000876
    8700006848
    ''',
    '''
    0050900866
    8500800575
    9900000039
    9700000041
    9935080063
    7712300000
    7911250009
    2211130000
    0421125000
    0021119000
    ''',
    '''
    2263031977
    0923031697
    0032221150
    0041111163
    0076191174
    0053411122
    0042361120
    5532241122
    1532247211
    1132230211
    ''',
    '''
    4484144000
    2044144000
    2253333493
    1152333274
    1187303285
    1164633233
    1153472231
    6643352233
    2643358322
    2243341322
    ''',
]


@pytest.fixture
def input_data():
    return [
        [[int(char) for char in line.strip()] for line in step.strip().split('\n')]
        for step in steps
    ]


@pytest.fixture
def file_input_data():
    with open('2021/day_11/input.txt', 'r') as f:
        return [[int(char) for char in line.strip()] for line in f.readlines()]


def test_simulate_step(input_data):
    current_map = None
    for step in input_data:
        if not current_map:
            current_map = step
            continue

        new_map = simulate_step(current_map)[0]
        assert new_map == step
        current_map = new_map


@pytest.mark.parametrize('steps, flashes', (
    (10, 204),
    (100, 1656),
))
def test_count_flashes_per_step(input_data, steps, flashes):
    assert count_flashes_per_step(input_data[0], steps) == flashes


def test_count_flashes_per_step_from_file(file_input_data):
    assert count_flashes_per_step(file_input_data, 100) == 1655


def test_find_all_flashed_simultaneously(input_data, file_input_data):
    assert find_all_flashed_simultaneously(input_data[0]) == 195
    assert find_all_flashed_simultaneously(file_input_data) == 337
