class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        seen = set(nums)
        answer = []
        for i in range(1, n + 1):
            if i not in seen:
                answer.append(i)
        
        return answer
