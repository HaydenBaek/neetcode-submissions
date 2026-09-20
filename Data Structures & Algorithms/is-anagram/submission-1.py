class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a1 = defaultdict(list)
        a2 = defaultdict(list)

        for i in s:

            if i in a1:
                a1[i] = a1[i] + 1
            else:
                a1[i] = 1

        for i in t:

            if i in a2:
                a2[i] = a2[i] + 1
            else:
                a2[i] = 1  

        return a1 == a2    
        
        
        