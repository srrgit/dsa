# 133. Clone Graph (Medium)
# Given a reference to a node in a connected undirected graph, return a deep copy
# (clone) of the graph. Each node contains a value and a list of neighbors.
# Approach: DFS/BFS with a hash map from original node -> cloned node; when
# visiting a node, create its clone (if not already created) and recursively
# clone/connect its neighbors. Time O(V + E), Space O(V).

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clones = {}

        def dfs(n: 'Node') -> 'Node':
            if n in clones:
                return clones[n]
            copy = Node(n.val)
            clones[n] = copy
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)


def build_graph(adj_list):
    """adj_list[i] (1-indexed via val) is the list of neighbor values for node i+1."""
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[v] for v in neighbors]
    return nodes[1]


def to_adj_list(start):
    if start is None:
        return []
    visited = {}
    order = []

    def dfs(n):
        if n.val in visited:
            return
        visited[n.val] = [nb.val for nb in n.neighbors]
        order.append(n.val)
        for nb in n.neighbors:
            dfs(nb)

    dfs(start)
    return [visited[v] for v in sorted(visited)]


if __name__ == "__main__":
    sol = Solution()
    original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned = sol.cloneGraph(original)

    assert to_adj_list(cloned) == [[2, 4], [1, 3], [2, 4], [1, 3]]
    assert cloned is not original
    assert cloned.val == original.val

    assert sol.cloneGraph(None) is None
    print("All tests passed.")
