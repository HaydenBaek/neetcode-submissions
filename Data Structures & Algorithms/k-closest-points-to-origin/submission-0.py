class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for point in points:

            x = point[0]
            y = point[1]

            closeScore = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(heap, (closeScore, point))
        
        answer = []
        for i in range(k):
            closeScore, point = heapq.heappop(heap)
            answer.append(point)
        
        return answer