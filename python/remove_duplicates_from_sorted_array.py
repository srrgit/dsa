# 26. Remove Duplicates from Sorted Array (Easy)
# Given a sorted integer array nums, remove the duplicates in-place so each
# unique element appears only once, keeping relative order, and return the
# number of unique elements k; the first k elements of nums should hold the
# final result.
#
# Approach: two-pointer in-place overwrite. `write` tracks the position for
# the next unique value; scan with `read` and whenever a new distinct value
# is found, copy it to nums[write] and advance write. Time: O(n),
# Space: O(1).

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    assert k1 == 2 and nums1[:k1] == [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    assert k2 == 5 and nums2[:k2] == [0, 1, 2, 3, 4]

    print("All test cases passed for 26. Remove Duplicates from Sorted Array")
