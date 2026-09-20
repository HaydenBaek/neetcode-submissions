class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  # sort by end
        removed = 0
        end = intervals[0][1]               # keep the earliest-ending interval

        for start, finish in intervals[1:]:  # skip the first one
            if start < end:                  # overlap → remove this one
                removed += 1
            else:                            # no overlap → keep it and move end
                end = finish

        return removed
