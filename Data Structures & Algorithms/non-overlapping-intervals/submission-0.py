class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:x[1])
        removed = 0
        end = intervals[0][0]
        for interval in intervals:
            start = interval[0]
            if start < end:
                removed += 1
            else:
                end = interval[1]
        return removed