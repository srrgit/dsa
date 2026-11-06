# 32. Longest Valid Parentheses (Hard)
# Given a string containing just the characters '(' and ')', find the
# length of the longest valid (well-formed) parentheses substring.
#
# Approach: stack of indices. Push index of every '(' and also push a
# "base" marker (-1) to simplify length computation. On ')', pop the stack;
# if the stack becomes empty, push current index as a new base, otherwise
# the current valid length is i - stack[-1]. Time: O(n), Space: O(n).


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestValidParentheses("(()") == 2
    assert sol.longestValidParentheses(")()())") == 4
    assert sol.longestValidParentheses("") == 0
    print("All test cases passed for 32. Longest Valid Parentheses")
