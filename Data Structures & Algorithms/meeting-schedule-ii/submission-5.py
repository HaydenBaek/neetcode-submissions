"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted([i.start for i in intervals ])
        end = sorted([i.end for i in intervals])

        result = 0
        count = 0
        startPtr = 0
        endPtr = 0

        while startPtr < len(intervals):
            if start[startPtr] < end[endPtr]:
                startPtr += 1
                count += 1
            else:   
                endPtr += 1
                count -= 1
            result = max(result, count)
        return result