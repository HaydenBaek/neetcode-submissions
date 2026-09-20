class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        counter = Counter(nums)

        common = counter.most_common()
        return common[0][0]