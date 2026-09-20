class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = Counter(nums)

        most_common = counter.most_common()
        print(most_common)
        return most_common[0][0]