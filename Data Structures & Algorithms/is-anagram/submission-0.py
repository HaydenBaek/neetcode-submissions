from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
           count = Counter(s)
           count1 = Counter(t)

           if count1 == count:
            return True
           return False 