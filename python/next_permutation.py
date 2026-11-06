# 31. Next Permutation (Medium)
# Given an array of integers, rearrange it in place into the lexicographically next greater
# permutation. If no such permutation exists (it is the largest permutation), rearrange it
# into the lowest possible order (sorted ascending).
# Approach: scan from the right to find the first index i where nums[i] < nums[i+1] (the
# "pivot"); if found, scan from the right again to find the first index j > i with
# nums[j] > nums[i], swap them, then reverse the suffix after i. If no pivot is found, the
# whole array is reversed (it was the last permutation). Time O(n), space O(1).

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    Solution().nextPermutation(nums1)
    assert nums1 == [1, 3, 2]

    nums2 = [3, 2, 1]
    Solution().nextPermutation(nums2)
    assert nums2 == [1, 2, 3]

    nums3 = [1, 1, 5]
    Solution().nextPermutation(nums3)
    assert nums3 == [1, 5, 1]
    print("All tests passed.")
