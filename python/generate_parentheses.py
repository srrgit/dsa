# 22. Generate Parentheses (Medium)
# Given n pairs of parentheses, return all combinations of well-formed (balanced) parentheses
# strings that can be formed using exactly n pairs.
# Approach: backtracking, adding '(' whenever the open-paren count is below n, and adding ')'
# whenever the close-paren count is below the open-paren count, building strings of length 2n.
# Time: O(4^n / sqrt(n)) (bounded by the nth Catalan number), Space: O(n) recursion depth.

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append("".join(current))
                return
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.generateParenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )
    assert sol.generateParenthesis(1) == ["()"]
    assert len(sol.generateParenthesis(4)) == 14  # 4th Catalan number
    print("All tests passed.")
