# 1021. Remove Outermost Parentheses (Easy)
# Given a non-empty valid parentheses string `s` that is a concatenation of
# "primitive" valid parentheses strings, remove the outermost parentheses of
# every primitive string and return the result.
#
# Approach: track a depth counter. A '(' is kept unless it takes depth from 0 to 1
# (an outermost open); a ')' is kept unless it takes depth from 1 to 0 (an
# outermost close). O(n) time, O(n) space for the output.


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(ch)
        return ''.join(result)


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeOuterParentheses("(()())(())") == "()()()"
    assert sol.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
    assert sol.removeOuterParentheses("()()") == ""
    print("All tests passed.")
