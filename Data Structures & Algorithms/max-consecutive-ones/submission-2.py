class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        answer = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
            else:
                answer = max(answer, current)
                current = 0
        return max(answer, current)