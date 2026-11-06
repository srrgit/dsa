# 417. Pacific Atlantic Water Flow (Medium)
# Given an m x n matrix of heights, water can flow from a cell to any 4-directionally adjacent
# cell with height less than or equal to the current cell's height. The Pacific Ocean touches the
# top and left edges of the matrix, the Atlantic touches the bottom and right edges. Return the
# coordinates of every cell from which water can flow to both oceans.
# Approach: reverse the flow direction and run multi-source BFS/DFS from each ocean's border
# cells, moving to neighbors with height >= current height; intersect the two reachable sets.
# Time: O(m*n), Space: O(m*n).

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                            (nr, nc) not in visited and
                            heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        stack.append((nr, nc))
            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = ([(rows - 1, c) for c in range(cols)] +
                            [(r, cols - 1) for r in range(rows)])

        pacific_reach = bfs(pacific_starts)
        atlantic_reach = bfs(atlantic_starts)

        result = [[r, c] for r, c in pacific_reach & atlantic_reach]
        return result


if __name__ == "__main__":
    sol = Solution()
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    expected = {(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)}
    result = sol.pacificAtlantic(heights)
    assert {tuple(x) for x in result} == expected
    assert sorted(sol.pacificAtlantic([[1]])) == [[0, 0]]
    print("All tests passed.")
