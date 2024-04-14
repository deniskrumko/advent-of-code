"""
https://leetcode.com/problems/remove-element
"""
from typing import List

import pytest


class Solution1:
    """Algoritmic solution.

    Complexity: O(n)
    Memory: O(n)
    Runtime 47 ms. Beats 5.42% of users with Python3 👎👎
    Memory 16.52 MB. Beats 48.92% of users with Python3 👍
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            if nums[i] == val:
                if nums[j] == val:
                    j -= 1
                    continue
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1

        return i


class Solution2:
    """Fast solution.

    Complexity: O(n*logn)
    Memory: O(n)
    Runtime 36 ms. Beats 64.35% of users with Python3 👍
    Memory 16.51 MB. Beats 48.92% of users with Python3 👍
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            return nums.sort(key=lambda x: 101 if x == val else x) or nums.index(val)
        except ValueError:
            return len(nums)


@pytest.mark.parametrize('solution, nums, val, expected_nums, expected_k', [
    (Solution1, [3, 2, 2, 3], 3, [2, 2], 2),
    (Solution1, [0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3], 5),
    (Solution1, [], 0, [], 0),
    (Solution1, [2], 3, [2], 1),
    (Solution2, [3, 2, 2, 3], 3, [2, 2], 2),
    (Solution2, [0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3], 5),
    (Solution2, [], 0, [], 0),
    (Solution2, [2], 3, [2], 1),
])
def test_removeElement(solution, nums, val, expected_nums, expected_k):
    k = solution().removeElement(nums, val)
    assert k == expected_k
    assert sorted(nums[:k]) == sorted(expected_nums)
