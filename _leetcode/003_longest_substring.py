"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""
import pytest


def get_length_of_longest_substring(s: str) -> int:
    subs, longest = '', 0
    for letter in s:
        if letter in subs:
            if len(subs) > longest:
                longest = len(subs)
            subs = subs[subs.index(letter) + 1:] + letter
        else:
            subs += letter

    return max(longest, len(subs))


@pytest.mark.parametrize('value, expected', (
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
))
def test_get_length_of_longest_substring(value, expected):
    assert get_length_of_longest_substring(value) == expected
