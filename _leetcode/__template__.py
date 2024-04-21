"""
__PROBLEM__
"""

import pytest


class Solution1:
    """First dumb solution.

    Complexity:
    Memory complexity:
    Runtime:
    Memory:
    """


# class Solution2:
#     """In-place solution. Better algoritmically.

#     Complexity:
#     Memory complexity:
#     Runtime:
#     Memory:
#     """


TEST_CASES = [
    (),  # noqa
    (),  # noqa
    (),  # noqa
]


@pytest.mark.parametrize("nums, expected_nums, expected_k", TEST_CASES)
def test_Solution1(nums, expected_nums, expected_k):
    n = nums[:]
    k = Solution1().removeDuplicates(n)
    assert k == expected_k
    assert sorted(n[:k]) == sorted(expected_nums)


# @pytest.mark.parametrize("nums, expected_nums, expected_k", TEST_CASES)
# def test_Solution2(nums, expected_nums, expected_k):
#     n = nums[:]
#     k = Solution2().removeDuplicates(n)
#     assert k == expected_k
#     assert sorted(n[:k]) == sorted(expected_nums)
