# 232. Implement Queue using Stacks (Easy)
# Implement a first-in-first-out (FIFO) queue using only two stacks, supporting push, pop, peek,
# and empty.
# Approach: an "in" stack receives pushes and an "out" stack serves pops/peeks; whenever "out" is
# empty, drain all of "in" into it, which reverses the order and restores FIFO behavior.
# Time: O(1) amortized per operation, Space: O(n).

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _transfer(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    q.push(3)
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.empty() is True
    print("All tests passed.")
