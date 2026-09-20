class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip()

        counter = 0

        index = len(s) - 1

        while index >= 0 and s[index] != " ":
            index -= 1
            counter += 1
        return counter