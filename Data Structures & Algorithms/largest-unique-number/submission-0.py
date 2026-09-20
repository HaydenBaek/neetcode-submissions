class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        counter = Counter(nums)

        appearing_once = []

        for key, freq in counter.items():
            if freq == 1:
                appearing_once.append((key, freq))
        
        if not appearing_once:
            return -1
        
        appearing_once.sort(key=lambda x:x[0], reverse = True)
        print(appearing_once)
        return appearing_once[0][0]