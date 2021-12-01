def count_measurement_increases(data: list):
    """Count measurement increases only."""
    return sum(data[i] > data[i-1] for i in range(1, len(data)))


def count_sliding_window_measurement_increases(data: list, window: int = 3):
    """Count sliding window measurement increases only."""
    window_sizes = [sum(data[i:window + i]) for i in range(len(data) - window + 1)]
    return count_measurement_increases(window_sizes)


if __name__ == '__main__':
    with open('2021/day_01/input.txt', 'r') as f:
        input_data = [int(i) for i in f.readlines()]
        print(f'Your result (1): {count_measurement_increases(input_data)}')
        print(f'Your result (2): {count_sliding_window_measurement_increases(input_data)}')
