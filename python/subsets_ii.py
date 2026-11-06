# 90. Subsets II (Medium)
# Given an integer array nums that may contain duplicates, return all possible subsets
# (the power set), without duplicate subsets.
# Approach: sort nums, then backtrack; at each decision point skip over duplicate values that
# were already considered at the same recursion depth so each duplicate subset is produced
# only once. Time O(2^n), space O(2^n) for the output.

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []

        def backtrack(start: int) -> None:
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    def normalize(subsets):
        return sorted(sorted(s) for s in subsets)

    assert normalize(Solution().subsetsWithDup([1, 2, 2])) == normalize(
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    )
    assert normalize(Solution().subsetsWithDup([0])) == normalize([[], [0]])
    print("All tests passed.")
