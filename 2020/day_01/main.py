from functools import reduce
from itertools import combinations


def expense_report(
    input_data: list,
    numbers_amount: int = 2,
    expteced_sum: int = 2020,
) -> int:
    """Calculate expense report."""
    for combination in combinations(input_data, numbers_amount):
        if sum(combination) == expteced_sum:
            return reduce(lambda x, y: x * y, combination)

    raise ValueError('No items match expected sum')


if __name__ == '__main__':
    with open('2020/day_01/input.txt', 'r') as f:
        input_data = [int(i) for i in f.readlines()]
        print(f'Your result (n = 2): {expense_report(input_data, 2)}')
        print(f'Your result (n = 3): {expense_report(input_data, 3)}')
