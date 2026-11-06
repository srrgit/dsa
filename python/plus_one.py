# 66. Plus One (Easy)
# Given a non-negative integer represented as an array of digits (most significant digit
# first), increment the number by one and return the resulting array of digits.
# Approach: walk from the last digit backwards, handle carries; if every digit was 9,
# prepend a 1. Time O(n), space O(n) for the output in the worst case.

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert Solution().plusOne([9]) == [1, 0]
    print("All tests passed.")
