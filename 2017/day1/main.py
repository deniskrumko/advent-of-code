def base_captcha(puzzle, increment):
    """Base function for captcha calculation.

    Args:
        puzzle (str): puzzle string
        increment (int): number to get next item to compare

    """
    result = 0

    for i, p in enumerate(puzzle):
        if puzzle[i] == puzzle[(i + increment) % len(puzzle)]:
            result += int(p)

    return result


def captcha_1(puzzle):
    """First captcha compares to next digit in string."""
    return base_captcha(puzzle=puzzle, increment=1)


def captcha_2(puzzle):
    """Second captcha compares to `len(puzzle)//2` digit in string."""
    return base_captcha(puzzle=puzzle, increment=len(puzzle) // 2)


def main():
    with open('day1/input.txt', 'r') as f:
        puzzle = f.readline().replace('\n', '')

    print('Captcha 1: {0}'.format(captcha_1(puzzle)))
    print('Captcha 2: {0}'.format(captcha_2(puzzle)))


if __name__ == '__main__':
    main()
