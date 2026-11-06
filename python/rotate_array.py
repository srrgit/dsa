# 189. Rotate Array (Medium)
# Given an integer array nums, rotate the array to the right by k steps,
# in-place.
#
# Approach: the "triple reversal" trick. Reverse the whole array, then
# reverse the first k elements and the remaining n-k elements separately.
# This produces the right rotation without extra array allocation.
# Time: O(n), Space: O(1).

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return

        def reverse(lo: int, hi: int) -> None:
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums1, 3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]

    nums2 = [-1, -100, 3, 99]
    sol.rotate(nums2, 2)
    assert nums2 == [3, 99, -1, -100]

    nums3 = [1, 2]
    sol.rotate(nums3, 3)
    assert nums3 == [2, 1]

    print("All test cases passed for 189. Rotate Array")
