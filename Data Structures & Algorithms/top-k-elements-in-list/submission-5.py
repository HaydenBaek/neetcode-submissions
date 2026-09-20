class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []

        counter = Counter(nums)

        for element, freq in counter.items():
            heapq.heappush(heap, (-freq, element))

        answer = []
        for i in range(k):
            freq, element = heapq.heappop(heap)
            answer.append(element)
        
        return answer
