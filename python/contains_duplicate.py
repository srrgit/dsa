# 217. Contains Duplicate (Easy)
# Given an integer array nums, return True if any value appears at least twice,
# and False if every element is distinct.
# Approach: insert elements into a set and compare its size to the array length
# (or short-circuit on first repeat). Time O(n), Space O(n).

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) is True
    assert sol.containsDuplicate([1, 2, 3, 4]) is False
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("All tests passed.")
