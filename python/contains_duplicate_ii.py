# 219. Contains Duplicate II (Easy)
# Given an integer array nums and an integer k, return true if there are two distinct
# indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.
# Approach: sliding window of size k using a hash set, checking membership before adding
# and evicting the element that falls out of the window. Time O(n), space O(min(n, k)).

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False


if __name__ == "__main__":
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) == True
    assert Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) == True
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
    print("All tests passed.")
