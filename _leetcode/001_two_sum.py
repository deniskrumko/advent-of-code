"""
https://leetcode.com/problems/two-sum/submissions/784002757/
"""
import pytest


def get_two_sum(nums: list[int], target: int) -> list[int]:
    indexes = {v: [i for i, x in enumerate(nums) if x == v] for v in nums}
    for a in sorted(indexes):
        b = target - a
        b_i = indexes.get(b)
        if b_i:
            a_i = indexes[a]
            return [a_i[0], b_i[-1]]

    raise ValueError('No result!')


@pytest.mark.parametrize('nums, target, expected', (
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
))
def test_get_two_sum(nums: list[int], target: int, expected: list[int]) -> None:
    assert get_two_sum(nums, target) == expected
