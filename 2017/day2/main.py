
def checksum_1(puzzle):
    """First checksum function."""
    result_sum = 0

    for row in puzzle:
        numbers = [int(x) for x in row.split()]
        max_number = max(numbers)
        min_number = min(numbers)
        difference = abs(max_number - min_number)
        result_sum += difference

    return result_sum


def checksum_2(puzzle):
    """Second checksum function."""
    result_sum = 0

    for row in puzzle:
        numbers = [int(x) for x in row.split()]

        for index_i, i in enumerate(numbers):
            for index_j, j in enumerate(numbers):
                if index_i == index_j:
                    continue

                if i % j == 0:
                    result_sum += i // j

    return result_sum


def main():
    with open('day2/input.txt', 'r') as f:
        puzzle = f.readlines()

    print('Checksum 1: {0}'.format(checksum_1(puzzle)))
    print('Checksum 2: {0}'.format(checksum_2(puzzle)))


if __name__ == '__main__':
    main()
