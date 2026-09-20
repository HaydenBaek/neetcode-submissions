class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        
        for right in range(1, len(s)):
            left = right - 1
            val = ord(s[left])
            val2 = ord(s[right])

            diff = abs(val - val2)

            score += diff

        
        return score

