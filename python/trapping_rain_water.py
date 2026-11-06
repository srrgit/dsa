# 42. Trapping Rain Water (Hard)
# Given n non-negative integers representing an elevation map where the width of
# each bar is 1, compute how much water it can trap after raining.
# Approach: two pointers from both ends tracking the max height seen so far on each
# side; move the pointer with the smaller max inward, accumulating trapped water.
# Time O(n), Space O(1).

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water


if __name__ == "__main__":
    sol = Solution()
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
    assert sol.trap([]) == 0
    print("All tests passed.")
