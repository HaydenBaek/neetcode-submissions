class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if len(self.nums) % 2 == 0:
            left = 0
            right = len(self.nums) - 1
            while left < right - 1:
                left += 1
                right -= 1
            midValue = (self.nums[left] + self.nums[right]) / 2
            return midValue
        else:
            left = 0
            right = len(self.nums) - 1
            mid = (left + right) // 2
            midValue = self.nums[mid]
            return midValue
        
        
        