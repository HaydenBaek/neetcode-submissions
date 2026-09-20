class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = nums[0]
        for i in range(len(nums)):

            if i == 0:
                continue
            
            p *= nums[i]
        
        if p > 0:
            return 1
        elif p < 0:
            return -1
        
        return 0