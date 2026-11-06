# 46. Permutations (Medium)
# Given an array nums of distinct integers, return all the possible permutations.
# Approach: backtracking; swap-in-place or build with a "used" set, recursing until
# the current permutation has the full length. Time O(n * n!), Space O(n) recursion
# plus O(n * n!) output.

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False] * n
        path: List[int] = []

        def backtrack() -> None:
            if len(path) == n:
                result.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack()
                    path.pop()
                    used[i] = False

        backtrack()
        return result


if __name__ == "__main__":
    sol = Solution()
    res = sol.permute([1, 2, 3])
    assert len(res) == 6
    expected = {(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)}
    assert {tuple(p) for p in res} == expected

    res2 = sol.permute([0, 1])
    assert sorted(res2) == [[0, 1], [1, 0]]
    print("All tests passed.")
