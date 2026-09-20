"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda i:i.start)
        meeting_rooms = 1
        heap = [intervals[0].end]
        for interval in intervals[1:]:
            if heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            meeting_rooms = max(meeting_rooms, len(heap))
        
        return meeting_rooms