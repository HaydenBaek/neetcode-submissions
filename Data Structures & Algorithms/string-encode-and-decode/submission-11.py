class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for i in strs:

            result += str(len(i)) + "#" + i
        return result


    def decode(self, s: str) -> List[str]:


        left = 0

        answer = []
        while left < len(s):
            right = left
            while right < len(s) and s[right] != "#":

                right += 1
            
            number = int(s[left: right])
            word = s[right + 1: right+1 + number]
            answer.append(word)
            left = 1+right + number

        return answer
            



