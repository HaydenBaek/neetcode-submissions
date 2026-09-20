class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        threshold = len(nums) // 3

        counter = Counter(nums)

        answer = []

        
        for key, freq in counter.items():
            if freq > threshold:
                answer.append(key)
        answer.sort()
        return answer