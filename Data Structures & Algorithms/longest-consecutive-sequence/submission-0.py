class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0

        for value in nums:
            if (value - 1) not in s:
                length = 0
                while (value + length) in s:
                    length = length + 1
                longest = max(length, longest)

        return longest       




        