class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        wordStorage = defaultdict(int)

        for i in s1:
            wordStorage[i] += 1
        
        left = 0
        right = 0
        n = len(s2)
        original = wordStorage.copy()

        while right < n:
            if s2[right] in wordStorage:
                wordStorage[s2[right]] -= 1
                if all(v == 0 for v in wordStorage.values()):
                    return True
                if any(v < 0 for v in wordStorage.values()):
                    wordStorage = original.copy()
                    right = left + 1
                    left = right
                    continue
            else:
                wordStorage = original.copy()
                left = right + 1
            right += 1
        
        return False