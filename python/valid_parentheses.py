# 20. Valid Parentheses (Easy)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid: every open bracket must be closed by the
# same type of bracket in the correct order.
# Approach: use a stack; push opening brackets, on a closing bracket pop and check
# it matches the expected opener. Time O(n), Space O(n).


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs.get(ch):
                    return False
        return not stack


if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("{[]}") is True
    print("All tests passed.")
