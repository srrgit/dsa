# 130. Surrounded Regions (Medium)
# Given an m x n board containing the characters 'X' and 'O', capture (flip to 'X') every region
# of 'O' that is completely surrounded by 'X' on all sides — i.e., not connected to any 'O' lying
# on the border of the board.
# Approach: DFS/BFS from every border 'O' cell to mark all 'O' cells connected to the border as
# safe; then flip every remaining (unmarked) 'O' to 'X', and finally restore safe cells back to
# 'O'.
# Time: O(m*n), Space: O(m*n) worst-case recursion stack.

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    sol.solve(board)
    assert board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]

    board2 = [["X"]]
    sol.solve(board2)
    assert board2 == [["X"]]
    print("All tests passed.")
