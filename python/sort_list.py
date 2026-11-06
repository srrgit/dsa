# 148. Sort List (Medium)
# Given the head of a linked list, return the list sorted in ascending order.
# Approach: recursive merge sort: split the list in half using a slow/fast pointer technique,
# recursively sort each half, then merge the two sorted halves.
# Time: O(n log n), Space: O(log n) recursion stack.

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self._merge(left, right)

    def _merge(self, a, b):
        dummy = ListNode()
        tail = dummy
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next


def build_list(values):
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


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    assert to_list(sol.sortList(build_list([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert to_list(sol.sortList(build_list([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
    assert to_list(sol.sortList(build_list([]))) == []
    print("All tests passed.")
