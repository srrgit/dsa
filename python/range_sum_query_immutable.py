# 303. Range Sum Query - Immutable (Easy)
# Design a class that, given an integer array, can answer multiple queries for the sum of
# elements between indices left and right inclusive.
# Approach: precompute a prefix-sum array once at construction time; each query is then a O(1)
# subtraction of two prefix sums. Construction O(n), each query O(1), space O(n).

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    assert num_array.sumRange(0, 2) == 1
    assert num_array.sumRange(2, 5) == -1
    assert num_array.sumRange(0, 5) == -3
    print("All tests passed.")
