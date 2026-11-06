# 301. Remove Invalid Parentheses (Hard)
# Given a string s containing letters and parentheses, remove the minimum number of
# invalid parentheses to make the input string valid, returning all possible results.
# Approach: BFS over strings reachable by deleting one character at a time; the first
# BFS level that contains at least one valid string is the minimal-removal level, and all
# valid strings found at that level are collected. Time O(2^n) worst case, space O(2^n).

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string: str) -> bool:
            balance = 0
            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        if is_valid(s):
            return [s]

        level = {s}
        while level:
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        candidate = string[:i] + string[i + 1:]
                        next_level.add(candidate)

            valid = [string for string in next_level if is_valid(string)]
            if valid:
                return valid
            level = next_level

        return [""]


if __name__ == "__main__":
    assert sorted(Solution().removeInvalidParentheses("()())()")) == sorted(["()()()", "(())()"])
    assert sorted(Solution().removeInvalidParentheses("(a)())()")) == sorted(["(a)()()", "(a())()"])
    assert Solution().removeInvalidParentheses(")(") == [""]
    print("All tests passed.")
