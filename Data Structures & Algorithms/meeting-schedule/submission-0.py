"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
# sort acc to the start times first
        intervals.sort(key = lambda i: i.start)

        n = len(intervals)
# now check if two consecutive meetings are having conflicts
        for i in range(1, n):
            i1, i2 = intervals[i - 1], intervals[i]
            if i2.start < i1.end:
                return False
        return True