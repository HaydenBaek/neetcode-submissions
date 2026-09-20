class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) < 2:
            return stones[0]

        heap = []

        for stone in stones:
            heapq.heappush_max(heap, stone)
        
        while len(heap) > 1:
            firstStone = heapq.heappop_max(heap)

            secondStone = heapq.heappop_max(heap)

            if firstStone == secondStone:
                continue
            newStone = abs(firstStone - secondStone)
            heapq.heappush_max(heap, newStone)
        
        if not heap:
            return 0
        return heap[0]