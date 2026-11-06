# 83. Remove Duplicates from Sorted List (Easy)
# Given the head of a sorted linked list, delete all duplicates such that each element
# appears only once, and return the sorted list.
# Approach: single pass, skipping forward past any node whose value equals the current
# node's value. Time O(n), space O(1).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


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
    assert to_list(Solution().deleteDuplicates(build([1, 1, 2]))) == [1, 2]
    assert to_list(Solution().deleteDuplicates(build([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert Solution().deleteDuplicates(None) is None
    print("All tests passed.")
