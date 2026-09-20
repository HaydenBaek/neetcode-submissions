"""
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        charCounter = {}
        #building counter
        for c in t:

            if c in charCounter:
                charCounter[c] += 1
            else:
                charCounter[c] = 1
        # ADOBECODEBANC
        # {A:2, B: 2, C: 2, N: 1 }


        left = 0
        right = 0
        required = len(t)
        shortestSubString = [0, float("inf")]

        while right < len(s):

            if s[right] in charCounter:
                if charCounter[s[right]] > 0:
                    required -= 1
                charCounter[s[right]] -= 1
            
            while required == 0:
                if (right - left) < (shortestSubString[1] - shortestSubString[0]):
                    shortestSubString = [left, right]
                
                if s[left] in charCounter:
                    charCounter[s[left]] += 1
                    if charCounter[s[left]] > 0:
                        required += 1
                left += 1
            
            right += 1
        
        left, right = shortestSubString
        if right == float("inf"):
            return ""
        
        return s[left:right+1]



        