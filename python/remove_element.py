# 27. Remove Element (Easy)
# Given an array nums and a value val, remove all occurrences of val in place and return the
# number of remaining elements k; the first k elements of nums should hold the result (order
# doesn't matter, and elements beyond index k are irrelevant).
# Approach: two-pointer in-place overwrite — a "write" pointer tracks where to place the next
# element that should be kept. Time O(n), space O(1).

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write


if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    k1 = Solution().removeElement(nums1, 3)
    assert k1 == 2 and sorted(nums1[:k1]) == [2, 2]

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = Solution().removeElement(nums2, 2)
    assert k2 == 5 and sorted(nums2[:k2]) == [0, 0, 1, 3, 4]
    print("All tests passed.")
