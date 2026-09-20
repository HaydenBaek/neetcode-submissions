class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        counter = Counter(s)
        m = 1
        for k, v in counter.items():
            m = max(m, v)
        
        if m < 2:
            return -1

        max_score = 0
        for i in range(len(s)):
            for j in range(i, len(s)):

                if s[i] == s[j]:
                    max_score = max(max_score, j - i - 1)

        return max_score
