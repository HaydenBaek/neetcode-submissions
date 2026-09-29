class Solution:
    def climbStairs(self, n: int) -> int:
        
        stairs = [0, 1, 2]



        for i in range(2, n):
            stairs.append(stairs[-1] + stairs[-2])
        
        return stairs[n]