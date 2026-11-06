# 739. Daily Temperatures (Medium)
# Given an array of daily temperatures, return an array `answer` where
# answer[i] is the number of days until a warmer temperature; if there is none,
# answer[i] = 0.
# Approach: monotonic decreasing stack of indices; when the current temperature
# exceeds the temperature at the index on top of the stack, pop it and record the
# day difference. Time O(n), Space O(n).

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # indices with temperatures awaiting a warmer day
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)
        return answer


if __name__ == "__main__":
    sol = Solution()
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    print("All tests passed.")
