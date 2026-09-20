class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        answer = ""

        smallest_string = ""
        smallest_length = float('inf')
        for s in strs:
            if len(s) < smallest_length:
                smallest_string = s
                smallest_length = len(s)
        
        for i in range(smallest_length):
            isValid = True
            for string in strs:
                if string[i] != smallest_string[i]:
                    isValid = False
                    return answer
            
            if isValid:
                answer += string[i]
                    

        return answer