from main import passphrase_check_1, passphrase_check_2


def tests():
    passphrase_1_tests = {
        'aa bb cc dd ee': True,
        'aa bb cc dd aa': False,
        'aa bb cc dd aaa': True
    }

    for test, result in passphrase_1_tests.items():
        assert passphrase_check_1(test) == result

    passphrase_2_tests = {
        'abcde fghij': True,
        'abcde xyz ecdab': False,
        'a ab abc abd abf abj': True,
        'iiii oiii ooii oooi oooo': True,
        'oiii ioii iioi iiio': False
    }

    for test, result in passphrase_2_tests.items():
        assert passphrase_check_2(test) == result


if __name__ == '__main__':
    tests()
    print('\nTests were successfully completed!')
