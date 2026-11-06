# 150. Evaluate Reverse Polish Notation (Medium)
# Evaluate the value of an arithmetic expression given in Reverse Polish Notation, where tokens
# are either integers or one of the operators +, -, *, /. Division between two integers truncates
# toward zero.
# Approach: stack-based evaluation; push operands onto the stack, and on encountering an operator
# pop the two most recent operands, apply the operator, and push the result back.
# Time: O(n), Space: O(n).

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for tok in tokens:
            if tok in ops:
                b = stack.pop()
                a = stack.pop()
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(tok))
        return stack[0]


if __name__ == "__main__":
    sol = Solution()
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    print("All tests passed.")
