# 36. Valid Sudoku (Medium)
# Given a 9x9 Sudoku board (with '.' for empty cells), determine if the filled
# cells satisfy the Sudoku rules: each row, column, and 3x3 sub-box contains
# each digit 1-9 at most once. (The board does not need to be solvable.)
#
# Approach: single pass over all 81 cells, tracking seen digits per row, per
# column, and per 3x3 box (indexed by (r//3, c//3)) using sets, checking for
# duplicates as we go. O(1) time/space since the board is fixed size (81
# cells).

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                box_idx = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        return True


if __name__ == "__main__":
    sol = Solution()
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert sol.isValidSudoku(board1) is True

    board2 = [row[:] for row in board1]
    board2[0][0] = "8"
    assert sol.isValidSudoku(board2) is False
    print("All tests passed.")
