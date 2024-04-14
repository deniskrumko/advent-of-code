"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array
"""

from typing import List

import pytest


class Solution1:
    """First dumb solution.

    Complexity: O(n*logn)
    Memory: O(2n) -> O(n)
    Runtime 75 ms. Beats 62.05% of users with Python3 👎
    Memory 17.86 MB. Beats 91.14% of users with Python3 👍
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        u = sorted(set(nums))
        nums[:] = u
        return len(u)


class Solution2:
    """In-place solution. Better algoritmically.

    Complexity: O(n)
    Memory: O(n)
    Runtime 69 ms. Beats 87.52% of users with Python3 👍
    Memory 18.01 MB. Beats 24.34% of users with Python3 👎 The fuck?
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[c] = nums[i]
                c += 1

        return c


@pytest.mark.parametrize(
    "solution, nums, expected_nums, expected_k",
    [
        (Solution1, [1, 1, 2], [1, 2], 2),
        (Solution1, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
        (Solution2, [1, 1, 2], [1, 2], 2),
        (Solution2, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
        (Solution2, [0], [0], 1),
        (Solution2, [], [], 0),
    ],
)
def test_removeElement(solution, nums, expected_nums, expected_k):
    k = solution().removeDuplicates(nums)
    assert k == expected_k
    assert sorted(nums[:k]) == sorted(expected_nums)
