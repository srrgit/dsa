# 47. Permutations II (Medium)
# Given an array nums that may contain duplicates, return all possible unique permutations in
# any order.
# Approach: sort nums, then backtrack while tracking which indices are used; to avoid duplicate
# permutations, skip picking nums[i] if it equals nums[i-1] and nums[i-1] has not been used in
# the current recursive branch (ensures identical values are only used in one relative order).
# Time O(n * n!), space O(n * n!) for the output.

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        used = [False] * n
        path = []
        result = []

        def backtrack() -> None:
            if len(path) == n:
                result.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return result


if __name__ == "__main__":
    def normalize(perms):
        return sorted(perms)

    assert normalize(Solution().permuteUnique([1, 1, 2])) == normalize(
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    )
    assert normalize(Solution().permuteUnique([1, 2, 3])) == normalize(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )
    print("All tests passed.")
