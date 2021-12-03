from copy import copy
from typing import Callable


def get_gamma_rate(data: list, parity: int = 0) -> str:
    """Get gamma rate for input data."""
    gamma_rate = ''
    for i in range(len(data[0])):
        result_bit = 0
        for j in range(len(data)):
            result_bit += (1 if data[j][i] == '1' else -1)
        gamma_rate += str(int(result_bit > 0) if result_bit != 0 else parity)
    return gamma_rate


def get_epsilon_rate(data: list, parity: int = 0) -> str:
    """Get epsilon rate for input data."""
    gamma_rate = get_gamma_rate(data, parity=int(not parity))  # inverse parity too
    gamma_rate_int = int(gamma_rate, 2)
    epsilon_rate_int = gamma_rate_int ^ int('1' * len(gamma_rate), 2)
    return f'{epsilon_rate_int:b}'.zfill(len(gamma_rate))


def get_power_consumption(data: list) -> int:
    """Find power consumption from diagnostic report."""
    gamma_rate = get_gamma_rate(data)
    epsilon_rate = get_epsilon_rate(data)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_life_support_rating_parameter(data: list, func: Callable, parity: int) -> str:
    """Get one specific parameter for life support rating."""
    initial = copy(data)

    for i in range(len(data[0])):
        passed = []
        gamma_total = func(initial, parity=parity)
        gamma_bit = gamma_total[i]
        for line in initial:
            if line[i] == gamma_bit:
                passed.append(line)

        initial = passed
        if len(passed) == 1:
            return passed[0]


def get_life_support_rating(data: list) -> int:
    """Get life support rating."""
    oxygen_rating = get_life_support_rating_parameter(data, func=get_gamma_rate, parity=1)
    co2_rating = get_life_support_rating_parameter(data, func=get_epsilon_rate, parity=0)
    return int(oxygen_rating, 2) * int(co2_rating, 2)


if __name__ == '__main__':
    with open('2021/day_03/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        print(f'Your result (1): {get_power_consumption(input_data)}')
        print(f'Your result (2): {get_life_support_rating(input_data)}')
