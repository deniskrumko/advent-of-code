from collections import Counter


def validator_1(password: str):
    """First validator."""
    return (
        ''.join(sorted(password)) == password
        and len(set(password)) < len(password)
    )


def validator_2(password: str):
    """Second validator."""
    return validator_1(password) and 2 in Counter(password).values()


class PasswordCracker:
    """Class to crack passwords."""

    def __init__(self, min_value, max_value, validator):
        """Initialize class instance."""
        self.min_value = min_value
        self.max_value = max_value
        self.validator = validator

    def get_password_variants_amount(self):
        """Get all password variants."""
        return len([
            value for value in range(self.min_value, self.max_value)
            if self.validator(str(value))
        ])


if __name__ == '__main__':
    min_password = 147981
    max_password = 691423
    print(f'Password range: {min_password} - {max_password}')

    cracker = PasswordCracker(min_password, max_password, validator_1)
    variants = cracker.get_password_variants_amount()
    print(f'First validator variants: {variants}')

    cracker = PasswordCracker(min_password, max_password, validator_2)
    variants = cracker.get_password_variants_amount()
    print(f'Second validator variants: {variants}')
