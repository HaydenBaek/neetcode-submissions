class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        most = counter.most_common(k)
        #[(a, 5)]   
        keys = [item[0] for item in most]
        return keys
        