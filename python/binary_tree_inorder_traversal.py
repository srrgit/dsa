# 94. Binary Tree Inorder Traversal (Easy)
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Approach: iterative traversal using an explicit stack, pushing left children until
# None then visiting and moving right. Time O(n), space O(h) for the stack (O(n) worst case).

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result


if __name__ == "__main__":
    # [1,null,2,3] -> [1,3,2]
    n3 = TreeNode(3)
    n2 = TreeNode(2, n3, None)
    n1 = TreeNode(1, None, n2)
    assert Solution().inorderTraversal(n1) == [1, 3, 2]

    # []
    assert Solution().inorderTraversal(None) == []

    # [1]
    assert Solution().inorderTraversal(TreeNode(1)) == [1]
    print("All tests passed.")
