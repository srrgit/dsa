# 297. Serialize and Deserialize Binary Tree (Hard)
# Design an algorithm to serialize a binary tree into a string, and deserialize that string back
# into the original tree structure.
# Approach: preorder DFS, encoding None children with a sentinel marker; deserialize by consuming
# tokens in the same preorder sequence recursively.
# Time: O(n) for both operations, Space: O(n).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []

        def dfs(node):
            if node is None:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))

        def build():
            val = next(tokens)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()


def to_list_preorder(root):
    out = []

    def dfs(node):
        if node is None:
            out.append(None)
            return
        out.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return out


if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    data = codec.serialize(root)
    result = codec.deserialize(data)
    assert to_list_preorder(result) == [1, 2, None, None, 3, 4, None, None, 5, None, None]

    empty = codec.deserialize(codec.serialize(None))
    assert empty is None

    single = codec.deserialize(codec.serialize(TreeNode(7)))
    assert single.val == 7 and single.left is None and single.right is None
    print("All tests passed.")
