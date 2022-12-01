import operator
from functools import reduce


class KnotHash:
    """Docstring"""

    def __init__(self, puzzle, numbers_range=256, make_ascii=True):
        """Custom `__init__` method."""
        if make_ascii:
            self.puzzle = KnotHash.to_ascii(puzzle)
        else:
            self.puzzle = [int(c) for c in puzzle.split(',')]

        self.list = list(range(numbers_range))
        self.size = numbers_range
        self.current = 0
        self.skip_size = 0

    def get_first_two(self):
        self.make_round()
        return self.list[0] * self.list[1]

    @classmethod
    def to_ascii(cls, line):
        return [ord(c) for c in line]

    def get_hash(self):
        self.puzzle += [17, 31, 73, 47, 23]

        for _ in range(64):
            self.make_round()

        dense = []
        for i in range(16):
            dense.append(KnotHash.xor_block(self.list[i * 16:(i + 1) * 16]))

        return KnotHash.to_hex(dense)

    def make_round(self):
        for p in self.puzzle:
            self.reverse_window(self.current, p)
            self.current = (self.current + p + self.skip_size) % self.size
            self.skip_size += 1

    @classmethod
    def to_hex(cls, num_list):
        return ''.join([str(hex(n)[2:]).zfill(2) for n in num_list])

    @classmethod
    def xor_block(cls, block):
        return reduce(lambda a, b: operator.xor(a, b), block, 0)

    def reverse_window(self, start, window):
        for i in range(window // 2):
            a = (start + i) % self.size
            b = (start - i + window - 1) % self.size
            self.list[a], self.list[b] = self.list[b], self.list[a]


if __name__ == '__main__':
    test_hash = KnotHash('3,4,1,5', numbers_range=5, make_ascii=False)
    assert test_hash.get_first_two() == 12

    with open('day10/input.txt', 'r') as f:
        puzzle = f.readline().replace('\n', '')

    print(KnotHash(puzzle, make_ascii=False).get_first_two())

    assert KnotHash.to_ascii('1,2,3') == [49, 44, 50, 44, 51]

    assert KnotHash.xor_block([
        65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22,
    ]) == 64

    assert KnotHash.to_hex([64, 7, 255]) == '4007ff'

    tests = {
        '': 'a2582a3a0e66e6e86e3812dcb672a272',
        'AoC 2017': '33efeb34ea91902bb2f59c9920caa6cd',
        '1,2,3': '3efbe78a8d82f29979031a4aa0b16a9d',
        '1,2,4': '63960835bcdc130f0b66d7ff4f6a5a8e',
    }

    for test, result in tests.items():
        assert KnotHash(test).get_hash() == result

    print(KnotHash(puzzle).get_hash())
