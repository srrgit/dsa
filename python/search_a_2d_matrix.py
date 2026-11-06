# 74. Search a 2D Matrix (Medium)
# Given an m x n matrix where rows are sorted ascending and the first integer of each row
# is greater than the last integer of the previous row, return whether target exists.
# Approach: treat the matrix as a single sorted array of length m*n and run binary search,
# converting the flat index to (row, col) with divmod. Time O(log(m*n)), space O(1).

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert Solution().searchMatrix(matrix, 3) == True
    assert Solution().searchMatrix(matrix, 13) == False
    print("All tests passed.")
