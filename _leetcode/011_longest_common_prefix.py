import pytest


def get_common_prefix(array) -> str:
    if len(array) == 1:
        return array[0]

    if len(array) == 2:
        common = ''
        len_arr_1 = len(array[1])
        for i in range(len(array[0])):
            if i == len_arr_1 or array[0][i] != array[1][i]:
                break
            common += array[0][i]
        return common

    left = get_common_prefix(array[:2])
    return get_common_prefix([left] + array[2:]) if left else ''


@pytest.mark.parametrize('value, expected', (
    (["flower", "flow", "flight"], 'fl'),
    (["dog", "racecar", "car"], ''),
    (["cir", "car"], 'c'),
))
def test_get_common_prefix(value, expected):
    assert get_common_prefix(value) == expected


# COOL SOLUTIONS FROM LEETCODE
# =============================================================================================

# 1. You need to compare only first and last elements in sorted list!

# class Solution1:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans

# 2. You can zip elements and check if they are the same!

# class Solution2:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         l = list(zip(*strs))
#         prefix = ""
#         for i in l:
#             if len(set(i))==1:
#                 prefix += i[0]
#             else:
#                 break
#         return prefix

# 3. Cool solution!

# class Solution3:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         pre = strs[0]
#         for i in strs:
#             while not i.startswith(pre):
#                 pre = pre[:-1]
#         return pre
