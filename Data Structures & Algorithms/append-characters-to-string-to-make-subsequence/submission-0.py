class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        ptr1 = 0
        ptr2 = 0
        answer = len(t)
        while ptr1 < len(s) and ptr2 < len(t):
            if s[ptr1] == t[ptr2]:
                answer -= 1
                ptr2 += 1
            ptr1 += 1
            
        return answer