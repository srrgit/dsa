# 155. Min Stack (Easy)
# Design a stack that supports push, pop, top, and retrieving the minimum element, all in
# constant time.
# Approach: an auxiliary field stored alongside each pushed value tracks the running minimum so
# far; each stack entry is a tuple (value, min_so_far_including_this_value).
# Time: O(1) per operation, Space: O(n).

class MinStack:
    def __init__(self):
        self.stack = []  # list of (value, min_so_far)

    def push(self, val: int) -> None:
        if self.stack:
            new_min = min(val, self.stack[-1][1])
        else:
            new_min = val
        self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2
    print("All tests passed.")
