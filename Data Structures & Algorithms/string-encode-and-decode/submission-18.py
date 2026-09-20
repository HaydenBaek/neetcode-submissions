class Solution:

    def encode(self, strs: List[str]) -> str:

        answer = ""

        for s in strs:
            answer += "#" + str(len(s)) + "#" + s

        return answer

    def decode(self, s: str) -> List[str]:

        left = 0
        answer = []
        n = len(s)

        while left < n: 
            if s[left] == "#":
                left += 1
                right = left

                while right < n and s[right] != "#":
                    right += 1
                
                number = int(s[left: right])
                right += 1
                string = s[right: right + number]
                answer.append(string)
                left = right + number
                
            
        return answer

