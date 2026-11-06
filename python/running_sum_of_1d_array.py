# 1480. Running Sum of 1d Array (Easy)
# Given an array `nums`, return its running sum, where runningSum[i] =
# sum(nums[0..i]).
#
# Approach: accumulate in place (or build a new list), adding each previous
# running total to the current element. O(n) time, O(n) space for the output.

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = nums[:]
        for i in range(1, len(result)):
            result[i] += result[i - 1]
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert sol.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert sol.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    print("All tests passed.")
