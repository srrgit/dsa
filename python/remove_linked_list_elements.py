# 203. Remove Linked List Elements (Easy)
# Given the head of a linked list and an integer val, remove all nodes with that value
# and return the new head.
# Approach: use a dummy sentinel node before head to simplify removal of the head itself,
# then walk the list unlinking any matching node. Time O(n), space O(1).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def build(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


if __name__ == "__main__":
    assert to_list(Solution().removeElements(build([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert Solution().removeElements(build([]), 1) is None
    assert to_list(Solution().removeElements(build([7, 7, 7, 7]), 7)) == []
    print("All tests passed.")
