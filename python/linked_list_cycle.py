# 141. Linked List Cycle (Easy)
# Given the head of a linked list, determine if the linked list has a cycle in it
# (some node can be reached again by continuously following next).
# Approach: Floyd's cycle detection (tortoise and hare) — a slow pointer moves one
# step and a fast pointer moves two steps; they meet if and only if there is a
# cycle. Time O(n), Space O(1).

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()

    # Cycle: 3 -> 2 -> 0 -> -4 -> back to node with value 2
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
    assert sol.hasCycle(n1) is True

    # No cycle: 1 -> 2
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    assert sol.hasCycle(a) is False

    assert sol.hasCycle(None) is False
    print("All tests passed.")
