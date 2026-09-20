class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        answer = []

        counter = Counter(nums)

        for element, freq in counter.items():
            
            if freq > len(nums) / 3:
                answer.append(element)
        
        return answer