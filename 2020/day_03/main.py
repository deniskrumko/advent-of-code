from functools import reduce


def traverse_map(input_data: list, right: int = 3, down: int = 1) -> int:
    """Traverse map and count all trees on the way."""
    x, y, count, line_length = 0, 0, 0, len(input_data[0])
    while y < len(input_data):
        if input_data[y][x % line_length] == '#':
            count += 1
        x += right
        y += down
    return count


def check_all_scopes(input_data: list) -> int:
    """Check all scopes of traversing the map and multiply trees amount."""
    scopes = [
        {'right': 1, 'down': 1},
        {'right': 3, 'down': 1},
        {'right': 5, 'down': 1},
        {'right': 7, 'down': 1},
        {'right': 1, 'down': 2},
    ]
    return reduce(lambda x, y: x * y, (traverse_map(input_data, **scope) for scope in scopes))


if __name__ == '__main__':
    with open('2020/day_03/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        print(f'Your result (1): {traverse_map(input_data)}')
        print(f'Your result (2): {check_all_scopes(input_data)}')
