# 174. Dungeon Game (Hard)
# A knight starts at the top-left of a dungeon grid (negative values are demons that cost
# health, non-negative values are potions that add health) and must reach the bottom-right,
# moving only right or down. The knight's health must stay above 0 at every room. Return the
# minimum initial health needed to guarantee reaching the destination.
# Approach: DP from the bottom-right backwards; need[r][c] is the minimum health required
# upon ENTERING cell (r, c) so that the knight can survive the rest of the path.
# need[r][c] = max(1, min(need[r+1][c], need[r][c+1]) - dungeon[r][c]). Time O(rows*cols),
# space O(rows*cols).

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        need = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows, -1, -1):
            for c in range(cols, -1, -1):
                if r == rows or c == cols:
                    need[r][c] = float("inf")
                elif r == rows - 1 and c == cols - 1:
                    need[r][c] = max(1, 1 - dungeon[r][c])
                else:
                    best_next = min(need[r + 1][c], need[r][c + 1])
                    need[r][c] = max(1, best_next - dungeon[r][c])
        return need[0][0]


if __name__ == "__main__":
    assert Solution().calculateMinimumHP(
        [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    ) == 7
    assert Solution().calculateMinimumHP([[0]]) == 1
    assert Solution().calculateMinimumHP([[100]]) == 1
    print("All tests passed.")
