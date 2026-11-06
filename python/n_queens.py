# 51. N-Queens (Hard)
# The n-queens puzzle asks for all distinct ways to place n queens on an
# n x n chessboard so that no two queens attack each other (same row,
# column, or diagonal). Return all solutions, each as a list of strings
# representing the board with 'Q' and '.'.
#
# Approach: backtracking, placing one queen per row. Track which columns
# and which diagonals (row - col and row + col) are already occupied with
# sets for O(1) conflict checks. Time: O(n!) in the worst case (bounded by
# the branching backtracking search), Space: O(n) for the recursion/column
# state plus O(n^2) per solution produced.

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        placement = [-1] * n  # placement[row] = col

        def backtrack(row: int) -> None:
            if row == n:
                board = []
                for r in range(n):
                    line = ["."] * n
                    line[placement[r]] = "Q"
                    board.append("".join(line))
                results.append(board)
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                placement[row] = col

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return results


if __name__ == "__main__":
    sol = Solution()

    solutions4 = sol.solveNQueens(4)
    assert len(solutions4) == 2
    expected4 = {(".Q..", "...Q", "Q...", "..Q."), ("..Q.", "Q...", "...Q", ".Q..")}
    actual4 = {tuple(board) for board in solutions4}
    assert actual4 == expected4

    solutions1 = sol.solveNQueens(1)
    assert solutions1 == [["Q"]]

    assert len(sol.solveNQueens(8)) == 92

    print("All test cases passed for 51. N-Queens")
