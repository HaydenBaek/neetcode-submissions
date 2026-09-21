class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(' ')

        pairs = {}
        seen = set()
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):

            c = pattern[i]
            word = words[i]
            if c in pairs:
                if pairs[c] != word:
                    return False
            else:
                if word in seen:
                    return False
                pairs[c] = word
            seen.add(word)
        
        return True
            
