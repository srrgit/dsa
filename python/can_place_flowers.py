# 605. Can Place Flowers (Easy)
# Given a flowerbed represented as a list of 0s (empty) and 1s (planted),
# and a number n, determine whether n new flowers can be planted such that
# no two flowers are adjacent.
#
# Approach: greedy left-to-right scan. For each plot, if it is empty and both
# neighbors (treating out-of-bounds as empty) are empty, plant a flower there
# and decrement n. Time: O(len(flowerbed)), Space: O(1) (a copy is avoided by
# checking bounds directly).

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n


if __name__ == "__main__":
    sol = Solution()
    assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True
    assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False
    assert sol.canPlaceFlowers([0, 0, 1, 0, 1], 1) is True
    print("All test cases passed for 605. Can Place Flowers")
