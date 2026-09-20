class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(' ')

        seen = set()

        pair = {}

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):

            word = words[i]
            if pattern[i] in pair:
                if not word == pair[pattern[i]]:
                    return False
            
            else:
                if word in seen:
                    return False
                pair[pattern[i]] = word
            seen.add(word)
        return True