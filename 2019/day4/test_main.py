import pytest

from .main import (
    PasswordCracker,
    validator_1,
    validator_2,
)


@pytest.mark.parametrize('password,is_valid', (
    ('111111', True),
    ('122345', True),
    ('111123', True),
    ('223450', False),
    ('123789', False),
))
def test_validator_1(password, is_valid):
    assert validator_1(password) == is_valid


@pytest.mark.parametrize('min_password,max_password,variants', (
    (147981, 691423, 1790),
))
def test_get_validator_1_variants(min_password, max_password, variants):
    cracker = PasswordCracker(min_password, max_password, validator_1)
    assert cracker.get_password_variants_amount() == variants


@pytest.mark.parametrize('password,is_valid', (
    ('112233', True),
    ('123444', False),
    ('111122', True),
    ('111222', False),
    ('122233', True),
    ('122334', True),
    ('122333', True),
))
def test_validator_2(password, is_valid):
    assert validator_2(password) == is_valid


@pytest.mark.parametrize('min_password,max_password,variants', (
    (147981, 691423, 1206),
))
def test_get_validator_2_variants(min_password, max_password, variants):
    cracker = PasswordCracker(min_password, max_password, validator_2)
    assert cracker.get_password_variants_amount() == variants
