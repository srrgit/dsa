# 977. Squares of a Sorted Array (Easy)
# Given an integer array nums sorted in non-decreasing order, return an
# array of the squares of each number, also sorted in non-decreasing
# order.
#
# Approach: two pointers from both ends. Since the array may contain
# negative numbers, the largest squares come from the extremes; compare
# |nums[left]| and |nums[right]|, place the larger square at the end of
# the result, and move the corresponding pointer inward. Time: O(n),
# Space: O(n) for the result.

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sol.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert sol.sortedSquares([0]) == [0]
    print("All test cases passed for 977. Squares of a Sorted Array")
