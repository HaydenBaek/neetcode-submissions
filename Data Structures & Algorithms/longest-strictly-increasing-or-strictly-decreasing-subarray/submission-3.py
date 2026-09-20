class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0    

        streak = 0
        largest = 1
        smallest = 1
        prev = nums[0]
        
        for n in nums:
            if n > prev:
                streak += 1

                largest = max(largest, streak + 1)
            else:
                streak = 0
            prev = n
        
        prev = nums[0]
        streak = 0

        for n in nums:
            if n < prev:
                streak += 1

                smallest = max(smallest, streak + 1)
            else:
                streak = 0
            prev = n


        return max(smallest, largest)

