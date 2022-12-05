"""
https://leetcode.com/problems/add-two-numbers/description/
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_val: Optional['ListNode'] = None):
        self.val = val
        self.next = next_val

    @classmethod
    def from_list(cls, values_list) -> 'ListNode':
        last_value = None
        for value in reversed(values_list):
            last_value = ListNode(val=value, next_val=last_value)
        return last_value

    def to_list(self):
        node = self
        while True:
            yield node.val
            node = node.next
            if not node:
                break


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    prev_node = None
    res_node = None
    over = 0

    while True:
        val_1 = l1.val if l1 else 0
        val_2 = l2.val if l2 else 0

        s = val_1 + val_2 + over
        if s >= 10:
            s %= 10
            over = 1
        else:
            over = 0

        cur_node = ListNode(val=s)
        if prev_node:
            prev_node.next = cur_node

        if res_node is None:
            res_node = cur_node

        prev_node = cur_node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        if not l1 and not l2 and not over:
            break

    return res_node


def test_add_two_numbers():
    l1 = ListNode.from_list([2, 4, 3])
    l2 = ListNode.from_list([5, 6, 4])

    result = add_two_numbers(l1, l2)
    assert list(result.to_list()) == [7, 0, 8]
