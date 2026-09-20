class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftArray = []
        rightArray = [0] * len(height)
        
        n = len(height)
        leftMax = height[0]
        rightMax = height[n - 1]

        for i in range(0, n, 1):
            leftArray.append(leftMax)
            leftMax = max(leftMax, height[i])
        
        for i in range(n - 1, -1, -1):
            rightArray[i] = rightMax
            rightMax = max(rightMax, height[i])
        
        totalWater = 0

        for i in range(n):
            minBar = min(leftArray[i], rightArray[i])

            water = minBar - height[i]

            if water < 0:
                continue
            
            totalWater += water
        
        return totalWater