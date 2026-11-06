# 160. Intersection of Two Linked Lists (Easy)
# Given the heads of two singly linked lists, return the node at which they intersect, or None if
# the two lists do not intersect.
# Approach: two pointers traverse both lists; when a pointer reaches the end of its list, redirect
# it to the head of the other list. They are guaranteed to meet at the intersection node (or both
# reach None) within len(A) + len(B) steps.
# Time: O(m + n), Space: O(1).

from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


if __name__ == "__main__":
    sol = Solution()
    # Build intersecting lists: A = 4->1->[8->4->5], B = 5->6->1->[8->4->5]
    common = ListNode(8, ListNode(4, ListNode(5)))
    a = ListNode(4, ListNode(1, common))
    b = ListNode(5, ListNode(6, ListNode(1, common)))
    assert sol.getIntersectionNode(a, b) is common

    # No intersection
    a2 = ListNode(2, ListNode(6, ListNode(4)))
    b2 = ListNode(1, ListNode(5))
    assert sol.getIntersectionNode(a2, b2) is None

    assert sol.getIntersectionNode(None, None) is None
    print("All tests passed.")
