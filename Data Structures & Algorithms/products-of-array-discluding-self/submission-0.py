class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
    
        check = 0
        while check < len(nums):
            
            add = 1
            pointer = 0
            while pointer < len(nums):
                if check != pointer:
                    add *= nums[pointer]
                    pointer += 1
                else:
                    pointer += 1
            result.append(add)
            check += 1
        
        return result



        