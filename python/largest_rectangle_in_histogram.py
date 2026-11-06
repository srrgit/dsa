# 84. Largest Rectangle in Histogram (Hard)
# Given an array of integers heights representing a histogram's bar heights where
# each bar has width 1, return the area of the largest rectangle that fits in the
# histogram.
# Approach: monotonic increasing stack of indices; when a shorter bar is found,
# pop taller bars and compute the rectangle area using the popped bar's height and
# a width spanning back to the new top of the stack (or the start). A sentinel 0
# height at the end flushes the stack. Time O(n), Space O(n).

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices, with heights[stack] increasing
        best = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                best = max(best, height * width)
            stack.append(i)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    assert sol.largestRectangleArea([1, 1]) == 2
    print("All tests passed.")
