# 169. Majority Element (Easy)
# Given an array nums of size n, return the majority element, the element that
# appears more than n/2 times (guaranteed to exist).
# Approach: Boyer-Moore voting algorithm — maintain a candidate and a count;
# increment when the current element matches the candidate, otherwise decrement,
# switching candidates when the count hits zero. Time O(n), Space O(1).

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


if __name__ == "__main__":
    sol = Solution()
    assert sol.majorityElement([3, 2, 3]) == 3
    assert sol.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert sol.majorityElement([1]) == 1
    print("All tests passed.")
