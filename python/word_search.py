# 79. Word Search (Medium)
# Given an m x n grid of characters and a string word, return True if word exists in the grid,
# constructed from letters of sequentially adjacent cells (horizontally or vertically neighboring),
# using each cell at most once.
# Approach: DFS/backtracking from every cell matching the first letter, marking visited cells in
# place and restoring them on backtrack.
# Time: O(m*n*4^L) worst case (L = len(word)), Space: O(L) recursion stack.

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            tmp = board[r][c]
            board[r][c] = "#"
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = tmp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert sol.exist([row[:] for row in board1], "ABCCED") is True
    assert sol.exist([row[:] for row in board1], "SEE") is True
    assert sol.exist([row[:] for row in board1], "ABCB") is False
    print("All tests passed.")
