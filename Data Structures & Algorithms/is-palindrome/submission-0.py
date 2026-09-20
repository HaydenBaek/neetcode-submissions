class Solution:
    def isPalindrome(self, s: str) -> bool:

        char = []

        

        for i in s:

            if i.isalnum():
                char.append(i.lower())
        
        left = 0
        right = len(char) - 1

        while left < right:

            if char[left] != char[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
        