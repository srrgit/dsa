# 239. Sliding Window Maximum (Hard)
# Given an array nums and a sliding window of size k moving from left to right across the array,
# return the maximum value in each window position.
# Approach: monotonic deque storing indices with strictly decreasing values; pop from the back
# while the new value is >= the back's value, and pop from the front when that index falls out of
# the window.
# Time: O(n), Space: O(k).

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # indices, values decreasing
        result = []
        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    assert sol.maxSlidingWindow([9, 11], 2) == [11]
    print("All tests passed.")
