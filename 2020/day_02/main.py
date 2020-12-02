from collections import Counter
from typing import (
    Callable,
    Tuple,
)


def extract_policy_and_password(line: str) -> Tuple[int, int, str, str]:
    """Parse policy and password from input line."""
    policy, password = line.split(':')
    policy_places, character = policy.split()
    policy_a, policy_b = [int(x) for x in policy_places.split('-')]
    return policy_a, policy_b, character, password.strip()


def check_password_policy(line: str) -> bool:
    """Check password policy (first variant)."""
    policy_a, policy_b, character, password = extract_policy_and_password(line)
    count = Counter(password)[character]
    return policy_a <= count <= policy_b


def check_updated_password_policy(line: str) -> bool:
    """Check password policy (second variant)."""
    policy_a, policy_b, character, password = extract_policy_and_password(line)
    return sum(password[i-1] == character for i in (policy_a, policy_b)) == 1


def count_passwords(check_function: Callable, input_data: list) -> int:
    """Count correct passwords for specific password check function."""
    return sum(check_function(line) for line in input_data)


if __name__ == '__main__':
    with open('2020/day_02/input.txt', 'r') as f:
        input_data = [line.strip() for line in f.readlines()]
        print(f'Your result (1): {count_passwords(check_password_policy, input_data)}')
        print(f'Your result (2): {count_passwords(check_updated_password_policy, input_data)}')
