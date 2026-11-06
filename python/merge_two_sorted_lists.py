# 21. Merge Two Sorted Lists (Easy)
# Given the heads of two sorted linked lists, merge them into one sorted linked
# list and return its head.
# Approach: use a dummy head and splice nodes from whichever list has the smaller
# current value, advancing that list's pointer; attach the remaining tail at the
# end. Time O(n + m), Space O(1) extra (excluding the output list itself).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    sol = Solution()
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    assert to_list(sol.mergeTwoLists(l1, l2)) == [1, 1, 2, 3, 4, 4]

    assert to_list(sol.mergeTwoLists(None, None)) == []
    assert to_list(sol.mergeTwoLists(None, build_list([0]))) == [0]
    print("All tests passed.")
