# 39. Combination Sum (Medium)
# Given an array of distinct integers candidates and a target, return all unique
# combinations of candidates where the chosen numbers sum to target. The same
# number may be chosen an unlimited number of times.
# Approach: backtracking over sorted candidates; at each step either reuse the
# current candidate (same index, since repeats are allowed) or move to the next
# one, pruning when the remaining target goes negative. Time O(2^target) worst
# case, Space O(target) recursion.

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path: List[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break
                path.append(c)
                backtrack(i, remaining - c)
                path.pop()

        backtrack(0, target)
        return result


if __name__ == "__main__":
    sol = Solution()
    res = sol.combinationSum([2, 3, 6, 7], 7)
    assert {tuple(sorted(c)) for c in res} == {(2, 2, 3), (7,)}

    res2 = sol.combinationSum([2, 3, 5], 8)
    assert {tuple(sorted(c)) for c in res2} == {(2, 2, 2, 2), (2, 3, 3), (3, 5)}
    print("All tests passed.")
