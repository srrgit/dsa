# 1512. Number of Good Pairs (Easy)
# Given an array of integers `nums`, return the number of "good pairs" (i, j)
# with i < j and nums[i] == nums[j].
#
# Approach: count occurrences of each value with a Counter; for a value
# appearing c times, it contributes c*(c-1)/2 good pairs. O(n) time, O(n)
# space.

from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        for count in Counter(nums).values():
            total += count * (count - 1) // 2
        return total


if __name__ == "__main__":
    sol = Solution()
    assert sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    assert sol.numIdenticalPairs([1, 1, 1, 1]) == 6
    assert sol.numIdenticalPairs([1, 2, 3]) == 0
    print("All tests passed.")
