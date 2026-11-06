# 437. Path Sum III (Medium)
# Given the root of a binary tree and an integer targetSum, return the number of paths that
# sum to targetSum, where a path can start and end at any node but must travel only downward
# (parent to child).
# Approach: DFS while maintaining a running prefix sum from the root to the current node and a
# hash map of prefix-sum frequencies seen along the current path; at each node, the number of
# valid paths ending here equals the count of ancestors whose prefix sum equals
# (current_prefix - targetSum). Backtrack the frequency map when leaving a node. Time O(n),
# space O(h).

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        def dfs(node: Optional[TreeNode], running_sum: int) -> int:
            if node is None:
                return 0
            running_sum += node.val
            count = prefix_counts[running_sum - targetSum]

            prefix_counts[running_sum] += 1
            count += dfs(node.left, running_sum)
            count += dfs(node.right, running_sum)
            prefix_counts[running_sum] -= 1

            return count

        return dfs(root, 0)


if __name__ == "__main__":
    # Tree: [10,5,-3,3,2,null,11,3,-2,null,1]
    root = TreeNode(
        10,
        TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
        TreeNode(-3, None, TreeNode(11)),
    )
    assert Solution().pathSum(root, 8) == 3

    # Tree: [5,4,8,11,null,13,4,7,2,null,null,5,1]
    root2 = TreeNode(
        5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
    )
    assert Solution().pathSum(root2, 22) == 3
    print("All tests passed.")
