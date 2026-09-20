class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        answer = nums[0]
        maxNum = nums[0]
        minNum = nums[0]

        for i in range(1, len(nums)):

            if nums[i] < 0:
                maxNum, minNum = minNum, maxNum
            
            currMax = maxNum * nums[i]
            currMin = minNum * nums[i]

            maxNum = max(nums[i], currMax)
            minNum = min(nums[i], currMin)
            answer = max(answer, maxNum)
        
        return answer