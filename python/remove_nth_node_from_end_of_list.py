# 19. Remove Nth Node From End of List (Medium)
# Given the head of a linked list, remove the nth node from the end of the list and return the head.
# Approach: dummy node + two pointers; advance "fast" n+1 steps ahead of "slow", then move both
# until fast reaches the end, leaving slow just before the node to remove.
# Time: O(n), Space: O(1).

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
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
    assert to_list(sol.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(sol.removeNthFromEnd(build_list([1]), 1)) == []
    assert to_list(sol.removeNthFromEnd(build_list([1, 2]), 1)) == [1]
    print("All tests passed.")
