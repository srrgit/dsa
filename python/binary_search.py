# 704. Binary Search (Easy)
# Given a sorted (ascending) array of distinct integers nums and a target value,
# return the index of target in nums, or -1 if it is not present.
# Approach: classic binary search, halving the search range each iteration.
# Time O(log n), Space O(1).

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert sol.search([5], 5) == 0
    print("All tests passed.")
