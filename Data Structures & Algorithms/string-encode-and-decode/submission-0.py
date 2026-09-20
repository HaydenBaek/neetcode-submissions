class Solution:

    def encode(self, strs: List[str]) -> str:

        bigString = ""
        for index in range(len(strs)):
            bigString = bigString + str(len(strs[index])) + "#" + strs[index]
        return bigString    
        
    4#neet 4#code4 #love4 #you -> neet
    def decode(self, s: str) -> List[str]:

        newList = []
        i = 0
        while i < len(s):
            part = s.index("#", i) #1
            length = int(s[i:part]) #0 - 1 which is 4
            newList.append(s[part + 1: part + 1 + length]) # 2 - 6
            i = part + 1 + length
        return newList    