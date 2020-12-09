from copy import deepcopy

import pytest

from .main import (
    get_fixed_program_result,
    get_modified_programs,
    run_program,
)

input_data = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip().split('\n')

input_data_2 = deepcopy(input_data)
input_data_2[7] = 'nop -4'


@pytest.mark.parametrize('value, expected', (
    (input_data, 5),
    (input_data_2, 8),
))
def test_run_program(value, expected):
    assert run_program(value, prevent_loop=True) == expected


@pytest.mark.parametrize('value, expected', (
    (input_data, 8),
    (input_data_2, 8),
))
def test_get_fixed_program_result(value, expected):
    assert get_fixed_program_result(value) == expected


def test_get_modified_programs():
    programs = list(get_modified_programs(input_data))
    assert len(programs) == 5
    assert programs[4] == input_data_2


def test_2020_day_08_input():
    with open('2020/day_08/input.txt', 'r') as f:
        input_data = f.readlines()
        assert run_program(input_data, prevent_loop=True) == 1137
        assert get_fixed_program_result(input_data) == 1125
