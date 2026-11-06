# 682. Baseball Game (Easy)
# Given a list of string operations representing a baseball game's scoring
# ("+" = sum of last two scores, "D" = double the last score, "C" = cancel/
# remove the last score, or a numeric string = a new score), return the sum of
# all scores on the record after applying all operations.
#
# Approach: simulate with a stack, pushing/popping/combining per operation.
# O(n) time, O(n) space.

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)


if __name__ == "__main__":
    sol = Solution()
    assert sol.calPoints(["5", "2", "C", "D", "+"]) == 30
    assert sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert sol.calPoints(["1"]) == 1
    print("All tests passed.")
