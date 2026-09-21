class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        pointer = 0
        for c in t:
            
            if pointer < len(s) and s[pointer] == c:
                pointer += 1

        if pointer < len(s):
            return False
        return True