# 105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
# Given two integer arrays `preorder` and `inorder` representing the preorder
# and inorder traversal of a binary tree with unique values, construct and
# return the tree.
#
# Approach: the first element of preorder is always the current subtree's
# root; its position in inorder splits the inorder array into left/right
# subtree spans. Use a hashmap from value -> inorder index for O(1) lookup,
# and a pointer into preorder (advanced as we build in preorder order) to
# avoid slicing. O(n) time, O(n) space.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_in_inorder = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(in_lo: int, in_hi: int) -> Optional[TreeNode]:
            if in_lo > in_hi:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = index_in_inorder[root_val]
            root.left = build(in_lo, mid - 1)
            root.right = build(mid + 1, in_hi)
            return root

        return build(0, len(inorder) - 1)


def tree_to_list(root: Optional[TreeNode]) -> List:
    # Level-order representation (with None gaps) for easy comparison in tests.
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    sol = Solution()
    tree = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree.val == 3
    assert tree.left.val == 9
    assert tree.right.val == 20
    assert tree.right.left.val == 15
    assert tree.right.right.val == 7

    tree2 = sol.buildTree([-1], [-1])
    assert tree2.val == -1 and tree2.left is None and tree2.right is None
    print("All tests passed.")
