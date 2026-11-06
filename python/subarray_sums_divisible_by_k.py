# 974. Subarray Sums Divisible by K (Medium)
# Given an integer array nums and an integer k, return the number of non-empty
# contiguous subarrays whose sum is divisible by k.
# Approach: track prefix sums modulo k in a hashmap of counts; two prefixes with the same
# remainder mean the subarray between them sums to a multiple of k. Time O(n), space O(k).

from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        prefix = 0
        result = 0
        for num in nums:
            prefix = (prefix + num) % k
            result += counts[prefix]
            counts[prefix] += 1
        return result


if __name__ == "__main__":
    assert Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5) == 7
    assert Solution().subarraysDivByK([5], 9) == 0
    print("All tests passed.")
