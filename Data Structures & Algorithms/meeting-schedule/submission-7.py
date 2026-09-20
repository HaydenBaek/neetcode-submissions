"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        if len(intervals) < 2:
            return True
        meetings = []
        for interval in intervals:
            start = interval.start
            end = interval.end

            if not meetings:
                meetings.append(interval)
                continue
            else:
                lastMeetingEndTime = meetings[-1].end
                if lastMeetingEndTime > start:
                    return False
            
            meetings.append(interval)
        
        return True

