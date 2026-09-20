class Solution:
    def firstUniqChar(self, s: str) -> int:
        

        counter = Counter(s)

        c = set()
        for k, v in counter.items():

            if v == 1:
                c.add(k)
        
        
        if len(c) < 1:
            return -1
        
        for i in range(len(s)):
            if s[i] in c:
                return i