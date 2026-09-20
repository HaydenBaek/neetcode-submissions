class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        idx1 = 0
        idx2 = 0
        answer = ""
        while idx1 < len(word1) and idx2 < len(word2):
            answer += word1[idx1] + word2[idx2]
            idx1 += 1
            idx2 += 1
        
        if idx1 < len(word1):
            answer += word1[idx1:]
        if idx2 < len(word2):
            answer += word2[idx2:]
        
        return answer