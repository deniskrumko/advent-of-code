import math

__all__ = (
    'calculate_extra_fuel',
    'calculate_fuel',
    'calculate_sum_extra_fuel',
    'calculate_sum_fuel',
)


def calculate_fuel(mass: int) -> int:
    """Calculate amount of fuel."""
    return math.floor(mass / 3) - 2


def calculate_sum_fuel(input_file: str):
    """Calculate sum amount of fuel for all modules."""
    with open(input_file, 'r') as f:
        return sum(calculate_fuel(mass=int(line)) for line in f)


def calculate_extra_fuel(mass: int) -> int:
    """Calculate amount of fuel with extra fuel too."""
    fuel = calculate_fuel(mass)
    return (fuel + calculate_extra_fuel(mass=fuel)) if fuel >= 1 else 0


def calculate_sum_extra_fuel(input_file: str):
    """Calculate sum amount of fuel for all modules w/ extra fuel."""
    with open(input_file, 'r') as f:
        return sum(calculate_extra_fuel(mass=int(line)) for line in f)


if __name__ == '__main__':
    input_file = '2019/day1/input.txt'
    print(f'Input file: {input_file}')
    print(f'Total fuel: {calculate_sum_fuel(input_file)}')
    print(f'Total fuel w/ extra: {calculate_sum_extra_fuel(input_file)}')
