# 25. Reverse Nodes in k-Group (Hard)
# Given the head of a linked list, reverse the nodes of the list k at a time and return the
# modified list. If the number of remaining nodes is not a multiple of k, leave those nodes as is.
# Approach: for each group of k nodes, first check there are enough nodes left, then reverse that
# group in place and reconnect it to the previous group's tail.
# Time: O(n), Space: O(1).

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        def get_kth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
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
    assert to_list(sol.reverseKGroup(build_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert to_list(sol.reverseKGroup(build_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert to_list(sol.reverseKGroup(build_list([1]), 1)) == [1]
    print("All tests passed.")
