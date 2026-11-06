# 560. Subarray Sum Equals K (Medium)
# Given an array of integers nums and an integer k, return the total number of
# contiguous subarrays whose sum equals k.
# Approach: track prefix sums in a hashmap counting occurrences; for each prefix sum s,
# the number of previous prefixes equal to s - k gives new subarrays ending here.
# Time O(n), space O(n).

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            result += counts[prefix - k]
            counts[prefix] += 1
        return result


if __name__ == "__main__":
    assert Solution().subarraySum([1, 1, 1], 2) == 2
    assert Solution().subarraySum([1, 2, 3], 3) == 2
    print("All tests passed.")
