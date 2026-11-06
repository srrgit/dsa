# 283. Move Zeroes (Easy)
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements, in-place.
# Approach: two-pointer — `write` marks where the next non-zero element should go;
# scan left to right and swap each non-zero element into position `write`.
# Time O(n), Space O(1).

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1


if __name__ == "__main__":
    sol = Solution()
    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0]

    nums2 = [0]
    sol.moveZeroes(nums2)
    assert nums2 == [0]

    nums3 = [1, 2, 3]
    sol.moveZeroes(nums3)
    assert nums3 == [1, 2, 3]
    print("All tests passed.")
