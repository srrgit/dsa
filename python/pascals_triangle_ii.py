# 119. Pascal's Triangle II (Easy)
# Given an integer `rowIndex` (0-indexed), return that row of Pascal's
# triangle.
#
# Approach: build the row iteratively in place, updating from right to left so
# each element only depends on values not yet overwritten this iteration:
# row[j] = row[j] + row[j-1]. O(rowIndex^2) time, O(rowIndex) space.

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row


if __name__ == "__main__":
    sol = Solution()
    assert sol.getRow(3) == [1, 3, 3, 1]
    assert sol.getRow(0) == [1]
    assert sol.getRow(1) == [1, 1]
    print("All tests passed.")
