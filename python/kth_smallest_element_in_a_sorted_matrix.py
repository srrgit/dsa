# 378. Kth Smallest Element in a Sorted Matrix (Medium)
# Given an n x n matrix where each row and column is sorted in ascending order, return
# the kth smallest element in the matrix.
# Approach: binary search on the value range [matrix[0][0], matrix[-1][-1]]; for each
# candidate mid, count elements <= mid in O(n) using a staircase walk, narrowing the range.
# Time O(n log(max-min)), space O(1).

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_le(x: int) -> int:
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    assert Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
    assert Solution().kthSmallest([[-5]], 1) == -5
    print("All tests passed.")
