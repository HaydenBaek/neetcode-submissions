class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return 0 if stones[0] == stones[1] else abs(stones[0] - stones[1])
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:

            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                newStone = stone1 - stone2
            else:
                newStone = stone2 - stone1

            heapq.heappush(heap, -newStone) 
        
        return -heap[0] if heap else 0