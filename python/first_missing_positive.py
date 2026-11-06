# 41. First Missing Positive (Hard)
# Given an unsorted integer array, return the smallest missing positive integer, achieving this in
# O(n) time using only O(1) extra space.
# Approach: cyclic sort / index-as-hash: for each position, repeatedly swap its value v (when
# 1 <= v <= n) to index v-1, until every in-range value lands at its "home" index. Then scan for
# the first index whose value doesn't match index+1 — that index+1 is the answer.
# Time: O(n), Space: O(1).

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == "__main__":
    sol = Solution()
    assert sol.firstMissingPositive([1, 2, 0]) == 3
    assert sol.firstMissingPositive([3, 4, -1, 1]) == 2
    assert sol.firstMissingPositive([7, 8, 9, 11, 12]) == 1
    print("All tests passed.")
