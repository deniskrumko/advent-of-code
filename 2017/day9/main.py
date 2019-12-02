import re


class StreamProcessing(object):

    def __init__(self, puzzle):
        """Initialization method."""
        self.puzzle = puzzle

    def get_score(self):
        self.remove_exclamations()
        self.remove_commas()
        self.remove_garbage()
        return self.count_groups()

    def get_garbage(self):
        self.remove_exclamations()
        return self._remove_pattern(pattern=r'<.*?>', collect=True)

    def remove_commas(self):
        self._remove_pattern(pattern=r',')

    def remove_exclamations(self):
        self._remove_pattern(pattern=r'!.')

    def remove_garbage(self):
        self._remove_pattern(pattern=r'<.*?>')

    def _remove_pattern(self, pattern, collect=False):
        collected = 0

        while True:
            match = re.search(pattern, self.puzzle)

            if not match:
                return collected

            if collect:
                span = match.span()
                collected += (span[1] - span[0] - 2)

            self.puzzle = self.puzzle[:match.start()] + \
                self.puzzle[match.end():]

    def count_groups(self):
        scores = []
        level = 1
        for p in self.puzzle:
            if p == '{':
                scores.append(level)
                level += 1
            if p == '}':
                level -= 1

        return sum(scores)


if __name__ == '__main__':

    with open('day9/input.txt', 'r') as f:
        puzzle = f.readline().replace('\n', '')

    tests = {
        '{}': 1,
        '{{{}}}': 6,
        '{{},{}}': 5,
        '{{{},{},{{}}}}': 16,
        '{<a>,<a>,<a>,<a>}': 1,
        '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
        '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
        '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3,
    }

    for test, result in tests.items():
        assert StreamProcessing(test).get_score() == result, test

    print(StreamProcessing(puzzle).get_score())

    tests = {
        '<>': 0,
        '<random characters>': 17,
        '<<<<>': 3,
        '<{!>}>': 2,
        '<!!>': 0,
        '<!!!>>': 0,
        '<{o"i!a,<{i<a>': 10
    }

    for test, result in tests.items():
        assert StreamProcessing(test).get_garbage() == result, test

    print(StreamProcessing(puzzle).get_garbage())
