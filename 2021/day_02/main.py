instructions_map = {
    'forward': (1, 0),
    'down': (0, 1),
    'up': (0, -1),
}


def parse_instructions(instructions: list):
    for instruction in instructions:
        step_command, step_size = instruction.split()
        yield (*instructions_map[step_command], int(step_size))


def sumbarine_path(instructions: list, x: int = 0, y: int = 0):
    for x_step, y_step, step_size in parse_instructions(instructions):
        x += x_step * step_size
        y += y_step * step_size

    return x * y


def sumbarine_path_with_aim(instructions: list, x: int = 0, y: int = 0, aim: int = 0):
    for x_step, aim_step, step_size in parse_instructions(instructions):
        aim += aim_step * step_size
        x += x_step * step_size
        y += x_step * step_size * aim

    return x * y


if __name__ == '__main__':
    with open('2021/day_02/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        print(f'Your result (1): {sumbarine_path(input_data)}')
        print(f'Your result (2): {sumbarine_path_with_aim(input_data)}')
