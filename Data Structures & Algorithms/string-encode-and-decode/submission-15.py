class Solution:

    def encode(self, strs: List[str]) -> str:

        answer = ""

        for s in strs:
            answer += str(len(s)) + "#" + s
        
        return answer

    def decode(self, s: str) -> List[str]:

        # 4#neet4#code4#love3#you

        result = []
        left = 0
        right = left
        
        while right < len(s):

            right = left

            while s[right] != "#":
                right += 1
            
            number = int(s[left:right])

            left = right + 1
            right = left + number

            word = s[left:right]
            left = right
            result.append(word)
        
        return result
