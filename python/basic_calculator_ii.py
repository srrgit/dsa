# 227. Basic Calculator II (Medium)
# Evaluate a string expression containing non-negative integers and the operators
# +, -, *, / (integer division truncating toward zero), with no parentheses, respecting
# standard operator precedence.
# Approach: single pass with a stack; track the current number and the previous operator. For
# '+'/'-' push the (signed) number onto the stack; for '*'/'/' pop the last pushed number,
# combine it with the current number, and push the result back, which naturally resolves
# precedence. Sum the stack at the end. Time O(n), space O(n).


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"
        n = len(s)

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and ch != " ") or i == n - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    prev = stack.pop()
                    stack.append(int(prev / num))  # truncate toward zero
                op = ch
                num = 0

        return sum(stack)


if __name__ == "__main__":
    assert Solution().calculate("3+2*2") == 7
    assert Solution().calculate(" 3/2 ") == 1
    assert Solution().calculate(" 3+5 / 2 ") == 5
    print("All tests passed.")
