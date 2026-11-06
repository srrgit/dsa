# 1235. Maximum Profit in Job Scheduling (Hard)
# Given arrays of job start times, end times, and profits, choose a subset of non-overlapping
# jobs (end time <= next start time) that maximizes total profit.
# Approach: sort jobs by end time; DP where dp[i] is the max profit using the first i jobs
# (sorted). For each job, binary search for the latest job whose end time <= this job's start
# time, and take max(skip, take). Time O(n log n), space O(n).

import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        n = len(jobs)
        ends = [job[0] for job in jobs]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            end, start, p = jobs[i - 1]
            j = bisect.bisect_right(ends, start, 0, i - 1)
            dp[i] = max(dp[i - 1], dp[j] + p)

        return dp[n]


if __name__ == "__main__":
    assert Solution().jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120
    assert Solution().jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]) == 150
    assert Solution().jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]) == 6
    print("All tests passed.")
