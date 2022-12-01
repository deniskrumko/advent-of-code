def parse_boarding_pass(boarding_pass: str, x_min=0, x_max=127, y_min=0, y_max=7) -> tuple:
    """Parse boarding pass string."""
    if not boarding_pass:
        return x_min, y_min

    command = boarding_pass[0]
    if command == 'F':
        x_max = int(x_max - ((x_max - x_min + 1) / 2))
    if command == 'B':
        x_min = int(x_min + ((x_max - x_min + 1) / 2))
    if command == 'L':
        y_max = int(y_max - ((y_max - y_min + 1) / 2))
    if command == 'R':
        y_min = int(y_min + ((y_max - y_min + 1) / 2))

    return parse_boarding_pass(boarding_pass[1:], x_min, x_max, y_min, y_max)


def get_seat_id(boarding_pass: str) -> int:
    """Get seat id from boarding pass string."""
    row, column = parse_boarding_pass(boarding_pass)
    return row * 8 + column


def get_max_seat_id(boarding_passes: list) -> int:
    """Get max seat id from list of boarding passes."""
    return max(get_seat_id(boarding_pass) for boarding_pass in boarding_passes)


def get_missing_seat_ids(boarding_passes: list) -> set:
    """Get missing seat ids from list of boarding passes."""
    seat_ids = {get_seat_id(boarding_pass) for boarding_pass in boarding_passes}
    all_seat_ids = set(range(min(seat_ids), max(seat_ids) + 1))
    return all_seat_ids - seat_ids


if __name__ == '__main__':
    with open('2020/day_05/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        print(f'Your result (1): {get_max_seat_id(input_data)}')
        print(f'Your result (2): {get_missing_seat_ids(input_data)}')
