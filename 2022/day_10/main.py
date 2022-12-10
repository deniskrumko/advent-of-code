from pathlib import Path

INPUT_FILE = Path(__file__).parent / 'input.txt'
LINE = 40


def draw_data(data: str, display: bool = False) -> bool:
    """Draw input data and calculate signal strength."""
    state = 0  # 0 - do nothing, 1 - addx, 2 - add accumulator
    X = 1
    acc = None
    strength = 0
    output = ''

    commands = ' '.join(data.splitlines()).split()
    checkpoints = set(range(20, 221, LINE))

    for cycle, command in enumerate(commands):
        if cycle in checkpoints:
            strength += cycle * X

        if state == 2:
            X += acc
            state = 0

        if state == 1:
            acc = int(command)
            state = 2

        if command == 'addx':
            state = 1

        output += '#' if (X - 1 <= cycle % 40 <= X + 1) else '.'
        if display and len(output) % LINE == 0:
            better_looking = output.replace('#', '█')
            print(better_looking[len(output) - LINE: len(output)])

    return strength, output


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {draw_data(input_data)[0]}')
        print('Your result (2): ')
        draw_data(input_data, display=True)
