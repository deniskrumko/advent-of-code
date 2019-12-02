import pytest

from .main import (
    calculate_extra_fuel,
    calculate_fuel,
)


@pytest.mark.parametrize('mass,fuel', [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
])
def test_calculate_fuel(mass, fuel):
    assert calculate_fuel(mass) == fuel


@pytest.mark.parametrize('mass,fuel', [
    (14, 2),
    (1969, 966),
    (100756, 50346),
])
def test_calculate_extra_fuel(mass, fuel):
    assert calculate_extra_fuel(mass) == fuel
