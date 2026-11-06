# 142. Linked List Cycle II (Medium)
# Given the head of a linked list, return the node where a cycle begins, or None if there
# is no cycle.
# Approach: Floyd's cycle detection with slow/fast pointers to find a meeting point inside
# the cycle, then advance a pointer from head and the meeting point in lockstep to find the
# cycle's start. Time O(n), space O(1).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                ptr = head
                while ptr is not slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None


if __name__ == "__main__":
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle back to index 1
    assert Solution().detectCycle(n1) is n2

    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    assert Solution().detectCycle(a) is None
    print("All tests passed.")
