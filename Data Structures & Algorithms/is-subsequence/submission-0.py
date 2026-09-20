class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(t) and ptr2 < len(s):
            if t[ptr1] == s[ptr2]:
                ptr2 += 1
            ptr1 += 1
        
        return True if ptr2 >= len(s) else False