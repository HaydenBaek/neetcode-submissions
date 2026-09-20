class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeros = 0
        ones = 0
        twos = 0

        for num in nums:

            match num:
                case 0:
                    zeros += 1
                case 1:
                    ones += 1
                case 2: 
                    twos += 1
        print(zeros, ones, twos)
        index = 0
        while index < zeros:
            nums[index] = 0
            index += 1
        
        while index < ones + zeros:
            nums[index] = 1
            index += 1
        
        while index < twos + ones + zeros:
            nums[index] = 2
            index += 1
        
        