# 143. Reorder List (Medium)
# Given a singly linked list L0->L1->...->Ln-1->Ln, reorder it in place to
# L0->Ln->L1->Ln-1->L2->Ln-2->... Approach: find the middle with slow/fast pointers,
# reverse the second half, then merge the two halves alternately. Time O(n), space O(1).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev

        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def build(vals):
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


if __name__ == "__main__":
    h = build([1, 2, 3, 4])
    Solution().reorderList(h)
    assert to_list(h) == [1, 4, 2, 3]

    h2 = build([1, 2, 3, 4, 5])
    Solution().reorderList(h2)
    assert to_list(h2) == [1, 5, 2, 4, 3]
    print("All tests passed.")
