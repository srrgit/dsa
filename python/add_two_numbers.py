# 2. Add Two Numbers (Medium)
# Two non-empty linked lists represent non-negative integers with digits
# stored in reverse order (each node holds a single digit). Add the two
# numbers and return the sum as a linked list in the same reversed-digit
# format.
#
# Approach: simulate elementary-school addition. Walk both lists
# simultaneously, summing corresponding digits plus a running carry, and
# append new nodes to a result list. Continue until both lists are
# exhausted and no carry remains. Time: O(max(m, n)), Space: O(max(m, n))
# for the output list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry, digit = divmod(total, 10)
            current.next = ListNode(digit)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


def build_list(values):
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    sol = Solution()

    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    assert to_list(sol.addTwoNumbers(l1, l2)) == [7, 0, 8]

    l3 = build_list([0])
    l4 = build_list([0])
    assert to_list(sol.addTwoNumbers(l3, l4)) == [0]

    l5 = build_list([9, 9, 9, 9, 9, 9, 9])
    l6 = build_list([9, 9, 9, 9])
    assert to_list(sol.addTwoNumbers(l5, l6)) == [8, 9, 9, 9, 0, 0, 0, 1]

    print("All test cases passed for 2. Add Two Numbers")
