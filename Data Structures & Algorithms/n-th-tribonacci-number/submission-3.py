class Solution:
    def tribonacci(self, n: int) -> int:
        
        trib = [0, 1, 1]

        for i in range(2, n):
            add = trib[i - 1] + trib[i - 2] + trib[i]

            trib.append(add)
        
        return trib[n]