# 1448. Count Good Nodes in Binary Tree (Easy)
# In a binary tree, a node X is "good" if, on the path from the root to X, no node has a value
# greater than X's value. Return the number of good nodes in the tree.
# Approach: DFS carrying the maximum value seen along the current path; a node is good if its
# value >= that running max. Time O(n), space O(h) for recursion.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
            if node is None:
                return 0
            count = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            return count

        return dfs(root, root.val if root else float("-inf"))


if __name__ == "__main__":
    # Tree: [3,1,4,3,null,1,5]
    root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    assert Solution().goodNodes(root) == 4

    # Tree: [3,3,null,4,2]
    root2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
    assert Solution().goodNodes(root2) == 3

    assert Solution().goodNodes(TreeNode(1)) == 1
    print("All tests passed.")
