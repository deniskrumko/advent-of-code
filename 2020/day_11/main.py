from collections import Counter

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def get_adjacent_seats(x, y, data):
    adjacent_seats = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            row, column = y + j, x + i
            if 0 <= row < len(data) and 0 <= column < len(data[0]):
                adjacent_seats.append(data[row][column])

    counter = Counter(adjacent_seats)

    return [counter[value] for value in [EMPTY, OCCUPIED, FLOOR]]


def run_simulation(data: list):
    new_data = [''] * len(data)

    for y, row in enumerate(data):
        for x, seat in enumerate(row):
            new_value = seat
            if seat != FLOOR:
                empty, occupied, floor = get_adjacent_seats(x, y, data)
                if seat == EMPTY and occupied == 0:
                    new_value = OCCUPIED
                elif seat == OCCUPIED and occupied >= 4:
                    new_value = EMPTY

            new_data[y] += new_value

    return new_data


def get_stabilized_model(input_data: str):
    model, last_model = input_data.split(), None

    while model != last_model:
        last_model = model
        model = run_simulation(model)

    return model


def get_stabilized_model_count(input_data: str):
    stabilized_model = get_stabilized_model(input_data)
    return Counter(''.join(stabilized_model))[OCCUPIED]


if __name__ == '__main__':
    with open('2020/day_11/input.txt', 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {get_stabilized_model_count(input_data)}')
