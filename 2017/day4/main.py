
def passphrase_check_1(passphrase):
    """Passphrase check 1 - all words are unique."""
    words = passphrase.split()
    unique_words = set(words)
    return len(words) == len(unique_words)


def passphrase_check_2(passphrase):
    """Passphrase check 1 - no anagrams between words."""
    words = passphrase.split()
    anagrams = [''.join(sorted(word)) for word in words]
    unique_anagrams = set(anagrams)
    return len(anagrams) == len(unique_anagrams)


def calculate_valid_passphrases(check, puzzle):
    """Calculate how many valid passphrases by specified check."""
    valid_passphrases = 0

    for line in puzzle:
        if check(line):
            valid_passphrases += 1

    return valid_passphrases


def main():
    with open('day4/input.txt', 'r') as f:
        puzzle = f.readlines()

    p1 = calculate_valid_passphrases(passphrase_check_1, puzzle)
    p2 = calculate_valid_passphrases(passphrase_check_2, puzzle)

    print('Passphrase 1 - valid amount is {}'.format(p1))
    print('Passphrase 2 - valid amount is {}'.format(p2))


if __name__ == '__main__':
    main()
