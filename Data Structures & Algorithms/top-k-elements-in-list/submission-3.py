class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        common = counter.most_common(k)

        keys = [keys for keys, _ in common]
        return keys
        