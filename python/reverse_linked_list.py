# 206. Reverse Linked List (Easy)
# Given the head of a singly linked list, reverse the list and return the new head.
# Approach: iterative pointer reversal, keeping prev/curr/next pointers.
# Time: O(n), Space: O(1).

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


def build_list(values: List[int]) -> Optional[ListNode]:
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    assert to_list(sol.reverseList(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(sol.reverseList(build_list([1, 2]))) == [2, 1]
    assert to_list(sol.reverseList(build_list([]))) == []
    print("All tests passed.")
