import pytest

from .main import (
    captcha_1,
    captcha_2,
)


@pytest.mark.parametrize('code, expected', (
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9),
))
def test_captcha_1(code, expected):
    assert captcha_1(code) == expected


@pytest.mark.parametrize('code, expected', (
    ('1212', 6),
    ('1221', 0),
    ('123425', 4),
    ('123123', 12),
    ('12131415', 4),
))
def test_captcha_2(code, expected):
    assert captcha_2(code) == expected
