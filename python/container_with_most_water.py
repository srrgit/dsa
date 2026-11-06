# 11. Container With Most Water (Medium)
# Given n non-negative integers representing heights of vertical lines drawn at each index, find
# two lines that, together with the x-axis, form a container that holds the most water, and
# return the maximum area.
# Approach: two pointers starting at both ends; always move the pointer at the shorter line
# inward, since moving the taller one inward could never increase (and can only decrease or keep)
# the area.
# Time: O(n), Space: O(1).

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            best = max(best, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    assert sol.maxArea([4, 3, 2, 1, 4]) == 16
    print("All tests passed.")
