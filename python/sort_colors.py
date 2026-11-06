# 75. Sort Colors (Medium)
# Given an array nums with n objects colored red (0), white (1), or blue
# (2), sort them in-place so objects of the same color are adjacent, in
# the order red, white, blue, without using a library sort.
#
# Approach: Dutch National Flag algorithm. Maintain three pointers: low
# (boundary for 0's), mid (current element), high (boundary for 2's).
# Swap 0's to the front, 2's to the back, and advance mid only when a 1 is
# seen or after a successful swap with low. Time: O(n), Space: O(1).

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


if __name__ == "__main__":
    sol = Solution()

    nums1 = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums1)
    assert nums1 == [0, 0, 1, 1, 2, 2]

    nums2 = [2, 0, 1]
    sol.sortColors(nums2)
    assert nums2 == [0, 1, 2]

    nums3 = [0]
    sol.sortColors(nums3)
    assert nums3 == [0]

    print("All test cases passed for 75. Sort Colors")
