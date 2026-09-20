class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        s1Count = Counter(s1)
        windowCount = Counter(s2[: len(s1)])

        if s1Count == windowCount:
            return True
        
        for i in range(len(s1), len(s2)):
            #adding the right char
            windowCount[s2[i]] += 1
            #remove left char
            leftChar = s2[i - len(s1)]
            windowCount[leftChar] -= 1
            if windowCount[leftChar] == 0:
                del windowCount[leftChar]
            if s1Count == windowCount:
                return True
        
        return False