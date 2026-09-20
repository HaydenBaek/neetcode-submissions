class Solution:
    def tribonacci(self, n: int) -> int:
        

        trib = [0, 1, 1]

        for i in range(3, n + 1):
            new_num = trib[i - 3] + trib[i - 2] + trib[i - 1]
            trib.append(new_num)
            print(trib)
        
        return trib[n]