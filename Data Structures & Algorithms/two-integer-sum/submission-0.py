class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] == target:
                    arr.append(i)
                    arr.append(k)
        return arr