"""
https://leetcode.com/problems/merge-sorted-array
"""
from typing import List

import pytest


class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """First dumb soltion.

        Complexity: O(m*logm + n)
        Memory: O(n)
        Runtime 44 ms. Beats 25.74% of users with Python3 👎
        Memory 16.59 MB. Beats 78.25% of users with Python3 👍
        """
        nums1[m:] = nums2
        nums1.sort()

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Memory inefficient solution, but fast.

        Complexity: O(m + n)
        Memory: O(2n) -> O(n)
        Runtime 32 ms. Beats 92.83% of users with Python3 👍👍
        Memory 16.84 MB. Beats 7.60% of users with Python3 👎👎
        """
        ai, bi = 0, 0
        result = [0] * (m + n)

        for i in range(m + n):
            left = nums1[ai] if ai < m else None
            right = nums2[bi] if bi < n else None
            if left is None or (right is not None and right < left):
                result[i] = right
                bi += 1
            else:
                result[i] = left
                ai += 1

        nums1[:] = result


@pytest.mark.parametrize('nums1, m, nums2, n, expected', (
    (
        [1, 2, 3, 0, 0, 0],
        3,
        [2, 5, 6],
        3,
        [1, 2, 2, 3, 5, 6],
    ),
    (
        [1, 2, 5, 6, 0, 0],
        4,
        [3, 3],
        2,
        [1, 2, 3, 3, 5, 6],
    ),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    (
        [1, 2, 4, 5, 6, 0],
        5,
        [3],
        1,
        [1, 2, 3, 4, 5, 6],
    ),
    (
        [1, 2, 4, 5, 6, 0, 0],
        5,
        [3, 3],
        2,
        [1, 2, 3, 3, 4, 5, 6],
    ),
    ([1, 2, 4, 5], 4, [], 0, [1, 2, 4, 5]),
    (
        [-1, 0, 0, 3, 3, 3, 0, 0, 0],
        6,
        [1, 2, 2],
        3,
        [-1, 0, 0, 1, 2, 2, 3, 3, 3],
    ),
    (
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        3,
        [-1, 1, 1, 1, 2, 3],
        6,
        [-1, 0, 0, 1, 1, 1, 2, 3, 3],
    ),
))
def test_merge(nums1, m, nums2, n, expected):
    n1 = nums1[:]
    Solution().merge1(n1, m, nums2, n)
    assert n1 == expected

    n2 = nums1[:]
    Solution().merge2(n2, m, nums2, n)
    assert n2 == expected
