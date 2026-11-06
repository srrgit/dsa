# 116. Populating Next Right Pointers in Each Node (Medium)
# Given a perfect binary tree, populate each node's next pointer to point to its next
# right node on the same level (or None for the rightmost node).
# Approach: use the already-established next pointers of the current level to traverse it
# while linking the next level's children, achieving O(1) extra space without a queue.
# Time O(n), space O(1).

from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        leftmost = root
        while leftmost and leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root


if __name__ == "__main__":
    n4, n5, n6, n7 = Node(4), Node(5), Node(6), Node(7)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    root = Node(1, n2, n3)
    Solution().connect(root)
    assert root.next is None
    assert n2.next is n3
    assert n3.next is None
    assert n4.next is n5
    assert n5.next is n6
    assert n6.next is n7
    assert n7.next is None
    print("All tests passed.")
