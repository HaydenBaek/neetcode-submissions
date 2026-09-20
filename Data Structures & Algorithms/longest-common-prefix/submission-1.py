class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest = ""

        smallest_length = min(len(s) for s in strs)
        
        for i in range(smallest_length):
            curr_char = strs[0][i]
            for s in strs:
                if curr_char != s[i]:
                  
                    return longest
            
    
            longest += curr_char

        return longest