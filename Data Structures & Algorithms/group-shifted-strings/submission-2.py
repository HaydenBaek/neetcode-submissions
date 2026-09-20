class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        difference = defaultdict(list)

        for s in strings:
            level = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1]))% 26
                
                level.append(diff)
            
            difference[tuple(level)].append(s)
            print(difference)
        answer = []

        for key, val in difference.items():
            answer.append(val)
        
        return answer
