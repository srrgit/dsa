# 300. Longest Increasing Subsequence (Medium)
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# Approach: patience sorting with binary search — maintain an array `tails` where
# tails[i] is the smallest possible tail value of an increasing subsequence of
# length i+1; for each num, binary-search for its insertion point and replace or
# extend. Time O(n log n), Space O(n).

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: List[int] = []
        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)


if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    print("All tests passed.")
