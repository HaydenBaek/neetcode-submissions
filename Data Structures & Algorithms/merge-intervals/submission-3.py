class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append(interval)
            
        return result

        