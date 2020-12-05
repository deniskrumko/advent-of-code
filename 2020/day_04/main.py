import re
from functools import partial
from typing import Generator


def validator(func):
    """Decorator to define validator."""
    def wrapper(*args, **kwargs):
        if not args and kwargs:  # prepare validator
            return partial(func, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@validator
def int_validator(value: str = None, min: int = None, max: int = None):
    """Validate that value is integer between min and max."""
    assert (min or 0) <= int(value) <= (max or float('inf'))


@validator
def height_validator(value: str):
    """Validate height string."""
    validators = {'cm': int_validator(min=150, max=193), 'in': int_validator(min=59, max=76)}
    int_value, unit = value[:-2], value[-2:]
    validators[unit](int_value)


@validator
def regexp_validator(value: str = None, regexp: str = None):
    """Validate that string matches pattern."""
    assert re.match(regexp, value)


@validator
def one_of_validator(value: str = None, choices: list = None):
    """Validate that value is one of choices."""
    assert value in choices


@validator
def length_validator(value: str = None, length: int = None):
    """Validate string length."""
    assert len(value) == length


REQUIRED_FIELDS: set = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
FIELD_VALIDATORS = {
    'byr': int_validator(min=1920, max=2002),
    'iyr': int_validator(min=2010, max=2020),
    'eyr': int_validator(min=2020, max=2030),
    'hgt': height_validator,
    'hcl': regexp_validator(regexp='#[0-9a-f]{6}$'),
    'ecl': one_of_validator(choices=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    'pid': [int_validator, length_validator(length=9)],
}


def passports_parser(input_data: str) -> Generator:
    """Parse passports data."""
    for passport_data in input_data.split('\n\n'):
        value_pairs = [value.split(':') for value in passport_data.split()]
        yield dict(value_pairs)


def required_fields_validator(passport: dict) -> bool:
    """Validate passport that all required fields are presented."""
    return REQUIRED_FIELDS & set(passport) == REQUIRED_FIELDS


def strict_fields_validator(passport: dict) -> bool:
    """Validate passport by field values."""
    try:
        for key, value in passport.items():
            validators: list = FIELD_VALIDATORS.get(key)
            if validators:
                if not isinstance(validators, list):
                    validators = [validators]
                for validator in validators:
                    validator(value)
    except Exception:
        return False
    else:
        return True


def is_valid_passport(passport: dict, validators: list) -> bool:
    """Check if passport is valid by all validators."""
    return all(validator(passport) for validator in validators)


def count_valid_passports(
    input_data: str,
    check_required: bool = True,
    check_fields: bool = False,
) -> int:
    validators = []
    if check_required:
        validators.append(required_fields_validator)
    if check_fields:
        validators.append(strict_fields_validator)

    if not validators:
        raise ValueError('Not validators specified')

    return sum(is_valid_passport(passport, validators) for passport in passports_parser(input_data))


if __name__ == '__main__':
    with open('2020/day_04/input.txt', 'r') as f:
        input_data = f.read()
        print(f'Your result (1): {count_valid_passports(input_data)}')
        print(f'Your result (2): {count_valid_passports(input_data, check_fields=True)}')
