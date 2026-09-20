class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        counter = Counter(nums)

        for element, freq in counter.items():
            if freq > n/2:
                return element
        
        