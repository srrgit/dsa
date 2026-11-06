# 138. Copy List with Random Pointer (Medium)
# A linked list where each node has an additional random pointer that
# points to any node in the list (or null). Return a deep copy of the
# list, with the copy's next/random pointers referencing nodes within the
# new copied list.
#
# Approach: two passes using a hashmap from original node -> cloned node.
# First pass: create a clone for every original node (values only).
# Second pass: wire up each clone's next and random pointers using the
# hashmap to translate original references into cloned ones.
# Time: O(n), Space: O(n) for the hashmap and the cloned list.

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        mapping = {}
        node = head
        while node:
            mapping[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            clone = mapping[node]
            clone.next = mapping.get(node.next)
            clone.random = mapping.get(node.random)
            node = node.next

        return mapping[head]


def build_list_with_random(pairs):
    # pairs: list of (val, random_index or None)
    nodes = [Node(val) for val, _ in pairs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, rand_idx) in enumerate(pairs):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0] if nodes else None


def to_pairs(head):
    index_of = {}
    node = head
    i = 0
    while node:
        index_of[node] = i
        node = node.next
        i += 1
    result = []
    node = head
    while node:
        rand_idx = index_of[node.random] if node.random else None
        result.append((node.val, rand_idx))
        node = node.next
    return result


if __name__ == "__main__":
    sol = Solution()

    head1 = build_list_with_random([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])
    copy1 = sol.copyRandomList(head1)
    assert to_pairs(copy1) == [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]
    # ensure it's a deep copy, not the same nodes
    assert copy1 is not head1 and copy1.next is not head1.next

    head2 = build_list_with_random([(1, 1), (2, 0)])
    copy2 = sol.copyRandomList(head2)
    assert to_pairs(copy2) == [(1, 1), (2, 0)]

    assert sol.copyRandomList(None) is None

    print("All test cases passed for 138. Copy List with Random Pointer")
