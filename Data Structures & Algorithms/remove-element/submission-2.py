class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        answer = 0

        non_value = 0
        index = 0

        for i in range(len(nums)):
            while non_value < len(nums) and nums[non_value] == val:
                non_value += 1
            
            if nums[i] != val:
                answer += 1
            
            if non_value < len(nums):
                nums[i] = nums[non_value]
            non_value += 1

            print(nums, non_value, answer)
        return answer


