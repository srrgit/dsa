# 118. Pascal's Triangle (Easy)
# Given an integer numRows, return the first numRows rows of Pascal's triangle, where
# each number is the sum of the two numbers directly above it.
# Approach: build each row iteratively from the previous row, with 1s at the edges and
# interior values as sums of adjacent pairs from the row above. Time O(numRows^2), space
# O(numRows^2).

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle


if __name__ == "__main__":
    assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert Solution().generate(1) == [[1]]
    print("All tests passed.")
