from functools import lru_cache


def fuel_consumption(data: list[int], position: int) -> int:
    """Get fuel consumption for all crabs to go to position (var 1)."""
    return sum(abs(i - position) for i in data)


@lru_cache(maxsize=1024 * 1024 * 2)
def count_moves_2(start, end):
    """Count amount of fuel to go from start to end position (var 2)."""
    return sum(range(abs(start - end) + 1))


def fuel_consumption_2(data: list[int], position: int) -> int:
    """Get fuel consumption for all crabs to go to position (var 2)."""
    return sum(count_moves_2(i, position) for i in data)


def find_min_fuel_consumption(data: list[int], variant: int) -> int:
    """Find min fuel consumption for selected variant."""
    func = {1: fuel_consumption, 2: fuel_consumption_2}[variant]
    position = min(range(max(data)), key=lambda i: func(data, i))
    return func(data, position)


if __name__ == '__main__':
    with open('2021/day_07/input.txt', 'r') as f:
        input_data = [int(i) for i in f.read().split(',')]
        print(f'Your result (1): {find_min_fuel_consumption(input_data, 1)}')
        print(f'Your result (2): {find_min_fuel_consumption(input_data, 2)}')
