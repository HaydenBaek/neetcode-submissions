class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0':
            return 0
        
        dp = [1, 1]
        for index, number in enumerate(s[1:], 2):
            ways = 0
            if number != '0':
                ways += dp[index - 1]
            if 10 <= int(s[index - 2] + number) <= 26:
                ways += dp[index-2]
            dp.append(ways)
        
        return dp[-1]
