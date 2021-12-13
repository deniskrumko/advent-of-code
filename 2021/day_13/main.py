def make_fold(paper: list, instruction: str) -> dict:
    """Make single fold by instruction."""
    fold_direction, fold_coordinate = instruction.split()[2].split('=')
    fold_coordinate = int(fold_coordinate)
    new_paper = {}

    for y, x in paper:
        current_coordinate = y if fold_direction == 'y' else x
        if current_coordinate < fold_coordinate:
            new_paper[(y, x)] = '#'
        elif current_coordinate > fold_coordinate:
            new_coordinate = fold_coordinate - (current_coordinate - fold_coordinate)
            new_dot = (new_coordinate, x) if fold_direction == 'y' else (y, new_coordinate)
            new_paper[new_dot] = '#'

    return new_paper


def read_instructions(data: list) -> tuple:
    """Parse instructions and build initial paper."""
    instuctions_index, paper = data.index(''), {}
    for dot in data[:instuctions_index]:
        i, j = (int(x) for x in dot.split(','))
        paper[(j, i)] = '#'

    return paper, data[instuctions_index + 1:]


def make_one_fold_and_count(data: list) -> int:
    """Make one fold and count dots on paper."""
    paper, instructions = read_instructions(data)
    return len(make_fold(paper, instructions[0]))


def make_all_folds(data: list) -> dict:
    """Make all folds by instruction."""
    paper, instructions = read_instructions(data)
    for instruction in instructions:
        paper = make_fold(paper, instruction)
    return paper


def make_all_folds_and_print(data: list) -> None:
    """Make all folds by instruction and print result paper."""
    paper = make_all_folds(data)
    for i in range(max(paper, key=lambda x: x[0])[0] + 1):
        for j in range(max(paper, key=lambda x: x[1])[1] + 1):
            value = '██' if (i, j) in paper else '  '
            print(value, end='')
        print()


if __name__ == '__main__':
    with open('2021/day_13/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        print(f'Your result (1): {make_one_fold_and_count(input_data)}')
        print('Your result (2):\n')
        make_all_folds_and_print(input_data)
