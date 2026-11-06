# 525. Contiguous Array (Medium)
# Given a binary array nums, return the length of the longest contiguous subarray containing
# an equal number of 0s and 1s.
# Approach: convert to a running sum where 0 counts as -1 and 1 counts as +1; two indices with
# the same running sum mean the subarray between them has an equal count of 0s and 1s. Track
# the first occurrence of each running-sum value in a hash map. Time O(n), space O(n).

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_index = {0: -1}
        running_sum = 0
        best = 0

        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1
            if running_sum in first_index:
                best = max(best, i - first_index[running_sum])
            else:
                first_index[running_sum] = i

        return best


if __name__ == "__main__":
    assert Solution().findMaxLength([0, 1]) == 2
    assert Solution().findMaxLength([0, 1, 0]) == 2
    assert Solution().findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]) == 6
    print("All tests passed.")
