# 167. Two Sum II - Input Array Is Sorted (Easy)
# Given a 1-indexed array of integers sorted in non-decreasing order, find two numbers that add up
# to a specific target and return their 1-indexed indices.
# Approach: two pointers starting at both ends of the sorted array, moving inward based on whether
# the current pair's sum is below or above the target.
# Time: O(n), Space: O(1).

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]
    assert sol.twoSum([-1, 0], -1) == [1, 2]
    print("All tests passed.")
