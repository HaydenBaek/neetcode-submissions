class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        counter = Counter(nums)
        print(nums)
        nums.sort(key=lambda x: (counter[x], -x))
        print(nums)
        return nums