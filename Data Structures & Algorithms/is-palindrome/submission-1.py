class Solution:
    def isPalindrome(self, s: str) -> bool:

        newS = ""
        
        for i in s:

            if i.isalnum():

                newS += i.lower()
            
        
        left = 0
        right = len(newS) - 1

        while left < right:

            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1
        
        return True