from copy import deepcopy
from typing import (
    Generator,
    Optional,
)


def run_program(program: list, prevent_loop: bool) -> Optional[int]:
    """Run program by instructions.

    :return: accumulator value if program executed correctly, otherwise - None.
    """
    history = []
    position, accumulator = 0, 0

    while True:
        if position >= len(program):  # Program finished correctly
            return accumulator

        if position in history:  # Program stuck in loop
            return accumulator if prevent_loop else None

        command, value = program[position].strip().split()
        jump = 1
        if command == 'acc':
            accumulator += int(value)
        if command == 'jmp':
            jump = int(value)

        history.append(position)
        position += jump


def get_modified_programs(input_data: list) -> Generator:
    """Get all variants of input data with replaced jmp and nop operations."""
    yield input_data  # First attempt is original unmodified program

    for i, line in enumerate(input_data):
        if 'jmp' in line:
            new_line = line.replace('jmp', 'nop')
        elif 'nop' in line:
            new_line = line.replace('nop', 'jmp')
        else:
            continue

        modified_program = deepcopy(input_data)
        modified_program[i] = new_line
        yield modified_program


def get_fixed_program_result(input_data) -> Optional[int]:
    """Find fixed program and get accumulator result from it."""
    for program in get_modified_programs(input_data):
        result = run_program(program, prevent_loop=False)
        if result is not None:
            return result


if __name__ == '__main__':
    with open('2020/day_08/input.txt', 'r') as f:
        input_data = f.readlines()
        print(f'Your result (1): {run_program(input_data, prevent_loop=True)}')
        print(f'Your result (2): {get_fixed_program_result(input_data)}')
