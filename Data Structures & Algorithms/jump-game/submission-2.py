class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i in range(len(nums)):
            
            current_max_jump = nums[i]
            if i > max_jump:
                return False 
            max_jump = max(max_jump, current_max_jump + i)

            if max_jump >= len(nums) - 1:
                return True
        
        return True
        