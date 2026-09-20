class Solution:
    def reverseString(self, nums: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(nums) - 1
        while left < right:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left += 1
            right -= 1
        