import operator
from functools import reduce
from typing import Generator


def parse_answers(input_data: str) -> Generator:
    """Parse input data with answers."""
    for group_answers in input_data.split('\n\n'):
        yield group_answers.split()


def get_answers_set(group_answers: list, unique: bool) -> set:
    """Get set of unique answers per group."""
    func = operator.or_ if unique else operator.and_
    return reduce(lambda x, y: func(set(x), set(y)), group_answers, set(group_answers[0]))


def get_sum_of_answers(input_data: str, unique: bool = False) -> int:
    """Get sum of unique/same answers for all groups."""
    return sum(len(get_answers_set(group, unique)) for group in parse_answers(input_data))


if __name__ == '__main__':
    with open('2020/day_06/input.txt', 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {get_sum_of_answers(input_data, unique=True)}')
        print(f'Your result (2): {get_sum_of_answers(input_data, unique=False)}')
