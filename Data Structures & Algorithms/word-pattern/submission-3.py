class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(' ')

        if len(words) != len(pattern):
            return False
        pair = {}
        check = set()
        for i in range(len(words)):

            c = pattern[i]
            word = words[i]
            

            if c in pair:
                if pair[c] != word:
                    return False
            else:
                if word in check:
                    return False    
                pair[c] = word
            check.add(word)

        return True