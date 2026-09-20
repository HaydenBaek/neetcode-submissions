class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for index, element in enumerate(nums):
            need = target- element

            if need in seen:
                return [seen[need], index]

            seen[element] = index