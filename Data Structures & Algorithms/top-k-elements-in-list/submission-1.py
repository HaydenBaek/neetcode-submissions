class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        most_k = counter.most_common(k)

        only = [k for k,_ in most_k]

        return only
        