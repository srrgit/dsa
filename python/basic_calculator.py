# 224. Basic Calculator (Hard)
# Implement a basic calculator to evaluate a string expression containing
# non-negative integers, '+', '-', '(', ')', and spaces (no multiplication
# or division).
#
# Approach: single pass with a stack used to handle nested parentheses.
# Keep a running result and current sign; when an operand is scanned,
# apply it; when '(' is seen, push the current result and sign so they can
# be restored, resetting for the sub-expression; when ')' is seen, combine
# the sub-expression's result back into the outer context.
# Time: O(n), Space: O(n) for the stack in the worst case of deep nesting.


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1  # 1 for '+', -1 for '-'

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch in "+-":
                result += sign * number
                number = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ")":
                result += sign * number
                number = 0
                result *= stack.pop()  # sign before the parenthesis
                result += stack.pop()  # result before the parenthesis
        result += sign * number
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.calculate("1 + 1") == 2
    assert sol.calculate(" 2-1 + 2 ") == 3
    assert sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23
    print("All test cases passed for 224. Basic Calculator")
