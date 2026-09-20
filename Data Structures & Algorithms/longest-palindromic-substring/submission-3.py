class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        n = len(s)
        def isPalindrome(left, right):

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return (left, right)
        
        answer = ""
        max_diff = 0
        for i in range(n - 1):

            l1, r1 = isPalindrome(i, i)
            l2, r2 = isPalindrome(i, i + 1)

            diff1 = r1 - l1
            print(l1, r1)
            if diff1 > max_diff:
                max_diff = diff1
                answer = s[l1 + 1: r1]
            
            diff2 = r2 - l2
            if diff2 > max_diff:
                max_diff = diff2
                answer = s[l2 + 1: r2]
            
        
        return answer