import heapq  # ← ✅ don't forget this

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Edge case: no meetings
        if not intervals:
            return 0

        # 1️⃣ Sort meetings by start time
        intervals.sort(key=lambda i: i.start)

        # 2️⃣ Initialize heap with the end time of the first meeting
        heap = [intervals[0].end]

        # Track the maximum number of rooms used at once
        meeting_rooms = 1

        # 3️⃣ Iterate through the remaining meetings
        for interval in intervals[1:]:
            # If the earliest meeting has ended before current starts, reuse that room
            if heap[0] <= interval.start:
                heapq.heappop(heap)
            
            # Add this meeting's end time to the heap
            heapq.heappush(heap, interval.end)

            # Track the peak number of rooms being used
            meeting_rooms = max(meeting_rooms, len(heap))

        # 4️⃣ Return the total rooms required
        return meeting_rooms
