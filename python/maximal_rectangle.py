# 85. Maximal Rectangle (Hard)
# Given a rows x cols binary matrix filled with 0's and 1's, find the area
# of the largest rectangle containing only 1's.
#
# Approach: treat each row as the base of a histogram, where heights[j]
# accumulates consecutive 1's in column j up to the current row (reset to 0
# on a 0). For each row, run the "largest rectangle in histogram" algorithm
# using a monotonic increasing stack of indices. Time: O(rows * cols),
# Space: O(cols).

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        best = 0

        def largest_rectangle_in_histogram(heights: List[int]) -> int:
            stack = []  # stack of indices, heights increasing
            max_area = 0
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] >= h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            return max_area

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            best = max(best, largest_rectangle_in_histogram(heights))
        return best


if __name__ == "__main__":
    sol = Solution()
    matrix1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    assert sol.maximalRectangle(matrix1) == 6
    assert sol.maximalRectangle([["0"]]) == 0
    assert sol.maximalRectangle([["1"]]) == 1
    print("All test cases passed for 85. Maximal Rectangle")
