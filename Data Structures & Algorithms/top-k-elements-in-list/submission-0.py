from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        sortedItems = [k for k, _ in count.most_common()]
        answer1 = []
        for i in range(k):
            answer1.append(sortedItems[i])
        return answer1

        