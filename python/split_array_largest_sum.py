# 410. Split Array Largest Sum (Hard)
# Given an integer array nums and an integer k, split nums into k non-empty contiguous
# subarrays so as to minimize the largest sum among the subarrays; return that minimized
# largest sum.
# Approach: binary search on the answer (the candidate largest sum), between max(nums) and
# sum(nums); for each candidate, greedily count how many subarrays are needed so that no
# subarray sum exceeds it, and shrink the search range based on whether that count exceeds k.
# Time O(n log(sum(nums))), space O(1).

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def subarrays_needed(max_sum: int) -> int:
            count = 1
            current = 0
            for num in nums:
                if current + num > max_sum:
                    count += 1
                    current = num
                else:
                    current += num
            return count

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if subarrays_needed(mid) > k:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    assert Solution().splitArray([7, 2, 5, 10, 8], 2) == 18
    assert Solution().splitArray([1, 2, 3, 4, 5], 2) == 9
    assert Solution().splitArray([1, 4, 4], 3) == 4
    print("All tests passed.")
