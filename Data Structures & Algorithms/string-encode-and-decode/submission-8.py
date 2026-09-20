class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for i in strs:

            result += str(len(i)) + "#" + i
        
        return result

    def decode(self, s: str) -> List[str]:


        answer = []

        left = 0
        right = 0

        while left < len(s):
            
            while s[right] != "#":
                right += 1
            
            #right will always be "#"
            length= int(s[left:right])

            left = right + 1
            right = left + length
            answer.append(s[left:right])
            left = right

        return answer

            

