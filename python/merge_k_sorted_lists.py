# 23. Merge k Sorted Lists (Hard)
# Given an array of k linked lists, each sorted in ascending order, merge them
# into one sorted linked list and return its head.
# Approach: push the head of each non-empty list into a min-heap keyed by value
# (with a tiebreaker index since ListNode is not comparable); repeatedly pop the
# smallest, append it to the result, and push its successor. Time O(N log k)
# where N is the total number of nodes, Space O(k).

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        tail = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    sol = Solution()
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert to_list(sol.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert to_list(sol.mergeKLists([])) == []
    assert to_list(sol.mergeKLists([None])) == []
    print("All tests passed.")
