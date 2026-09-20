class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for i in strs:

            result = result + str(len(i)) + "#" + i
        
        return result

    def decode(self, s: str) -> List[str]:


        result = []

        pointer = 0

        while pointer < len(s):

            temp_pointer = pointer

            while s[temp_pointer] != "#":
                temp_pointer = temp_pointer + 1
            
            length = int(s[pointer: temp_pointer])

            string = s[temp_pointer + 1: temp_pointer + 1 + length]
            result.append(string)
            pointer = temp_pointer + 1 + length

        
        return result