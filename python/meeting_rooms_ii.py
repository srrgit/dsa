# 253. Meeting Rooms II (Medium)
# Given an array of meeting time intervals, return the minimum number of conference rooms
# required so that all meetings can be held without overlap.
# Approach: sort start times and end times separately; sweep through, incrementing a counter of
# rooms currently in use whenever a meeting starts before the earliest ongoing meeting ends, and
# decrementing (advancing the end pointer) once that earliest meeting finishes.
# Time: O(n log n), Space: O(n).

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        rooms = 0
        max_rooms = 0
        s_ptr = e_ptr = 0
        n = len(intervals)
        while s_ptr < n:
            if starts[s_ptr] < ends[e_ptr]:
                rooms += 1
                s_ptr += 1
                max_rooms = max(max_rooms, rooms)
            else:
                rooms -= 1
                e_ptr += 1
        return max_rooms


if __name__ == "__main__":
    sol = Solution()
    assert sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert sol.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert sol.minMeetingRooms([]) == 0
    print("All tests passed.")
