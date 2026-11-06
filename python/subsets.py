# 78. Subsets (Medium)
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# Approach: backtracking — at each index decide to include or exclude nums[i],
# recording the current path as a complete subset at every recursive call.
# Time O(n * 2^n), Space O(n) recursion plus O(n * 2^n) output.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path: List[int] = []

        def backtrack(start: int) -> None:
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    res = sol.subsets([1, 2, 3])
    assert len(res) == 8
    expected = {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}
    assert {tuple(s) for s in res} == expected

    res2 = sol.subsets([0])
    assert sorted(res2) == [[], [0]]
    print("All tests passed.")
