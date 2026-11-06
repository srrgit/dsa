# 240. Search a 2D Matrix II (Medium)
# Given an m x n matrix where each row is sorted in ascending order left to right and each
# column is sorted in ascending order top to bottom, determine whether a target value exists.
# Approach: start at the top-right corner; if the current value is larger than target, move
# left (eliminate the column), if smaller, move down (eliminate the row), if equal, found.
# Time O(m + n), space O(1).

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1
        while r < rows and c >= 0:
            value = matrix[r][c]
            if value == target:
                return True
            if value > target:
                c -= 1
            else:
                r += 1
        return False


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert Solution().searchMatrix(matrix, 5) is True
    assert Solution().searchMatrix(matrix, 20) is False
    print("All tests passed.")
