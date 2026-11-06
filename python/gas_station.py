# 134. Gas Station (Medium)
# There are n gas stations in a circle, each with gas[i] fuel and costing
# cost[i] to travel to the next station. Starting with an empty tank at
# some station, determine the starting index from which a car can complete
# the full circuit, or return -1 if impossible (the answer is guaranteed
# unique if one exists).
#
# Approach: greedy single pass. If the total gas is less than total cost,
# no solution exists. Otherwise, track a running tank balance while
# tentatively starting at index 0; whenever the balance goes negative, the
# current start candidate is invalid, so reset the candidate to the next
# station and the tank to 0. Time: O(n), Space: O(1).

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start


if __name__ == "__main__":
    sol = Solution()
    assert sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    assert sol.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4
    print("All test cases passed for 134. Gas Station")
