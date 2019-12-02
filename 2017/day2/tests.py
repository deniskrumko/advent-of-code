from main import checksum_1, checksum_2


def tests():
    checksum_1_input = (
        "5 1 9 5",
        "7 5 3",
        "2 4 6 8"
    )

    assert checksum_1(checksum_1_input) == 18

    checksum_2_input = (
        "5 9 2 8",
        "9 4 7 3",
        "3 8 6 5",
    )

    assert checksum_2(checksum_2_input) == 9


if __name__ == '__main__':
    tests()
    print('\nTests were successfully completed!')
