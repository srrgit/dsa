# 876. Middle of the Linked List (Easy)
# Given the head of a singly linked list, return the middle node of the
# linked list. If there are two middle nodes, return the second middle node.
#
# Approach: classic slow/fast two-pointer technique. The fast pointer moves
# two steps for every one step of the slow pointer; when fast reaches the
# end, slow is at the middle (the second middle for even-length lists).
# Time: O(n), Space: O(1).

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def build_list(values):
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    sol = Solution()

    head1 = build_list([1, 2, 3, 4, 5])
    assert to_list(sol.middleNode(head1)) == [3, 4, 5]

    head2 = build_list([1, 2, 3, 4, 5, 6])
    assert to_list(sol.middleNode(head2)) == [4, 5, 6]

    head3 = build_list([1])
    assert to_list(sol.middleNode(head3)) == [1]

    print("All test cases passed for 876. Middle of the Linked List")
