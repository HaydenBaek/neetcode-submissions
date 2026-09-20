class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        

        sort = sorted(nums)

        a = sort[0] * sort[1]
        b = sort[len(sort) - 1] * sort[len(sort) - 2] 
        return b - a
