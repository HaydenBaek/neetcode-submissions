class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current = nums[0]
        maxNumber = current

        for i in range(1, len(nums)):

            if current < 0:
                current = nums[i]
            else:
                current += nums[i]
            
            maxNumber = max(maxNumber, current)
        
        return maxNumber

        