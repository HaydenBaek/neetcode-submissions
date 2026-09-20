class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num = set(nums)
        length = 0
        answer = 0
        #find the start
        for n in num:

            if n - 1 not in num:
                length = 1

                while n + length in num:
                    length += 1
                answer = max(answer, length)
                
        return answer