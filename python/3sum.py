# 15. 3Sum (Medium)
# Given an integer array nums, return all unique triplets [nums[i], nums[j],
# nums[k]] such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
# Approach: sort the array; fix each element as the smallest of the triplet, then
# use a two-pointer scan on the remaining sorted subarray to find pairs summing to
# -nums[i], skipping duplicates at every level. Time O(n^2), Space O(1) extra
# (excluding sort/output).

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    res = sol.threeSum([-1, 0, 1, 2, -1, -4])
    assert {tuple(t) for t in res} == {(-1, -1, 2), (-1, 0, 1)}

    assert sol.threeSum([0, 1, 1]) == []
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]
    print("All tests passed.")
