class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        storage = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in storage:
                return [storage[complement], i]
            else:
                storage[nums[i]] = i
        
        return []
        