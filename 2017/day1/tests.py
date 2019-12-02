from main import captcha_1, captcha_2


def tests():
    captcha_1_tests = {
        '1122': 3,
        '1111': 4,
        '1234': 0,
        '91212129': 9
    }

    for puzzle, result in captcha_1_tests.items():
        assert captcha_1(puzzle) == result

    captcha_2_tests = {
        '1212': 6,
        '1221': 0,
        '123425': 4,
        '123123': 12,
        '12131415': 4
    }

    for puzzle, result in captcha_2_tests.items():
        assert captcha_2(puzzle) == result


if __name__ == '__main__':
    tests()
    print('\nTests were successfully completed!')
