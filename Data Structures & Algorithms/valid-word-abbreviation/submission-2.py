class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        answer = []
        i = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                if abbr[i] == "0":
                    return False
                digit = ""
                while i < len(abbr) and abbr[i].isdigit():
                    digit += abbr[i]
                    i += 1
                    
                answer.append(int(digit))
                continue
                
            else:
                answer.append(abbr[i])
            i += 1
            print(answer ,i, len(abbr))
        string = ""
        for i in answer:
            if type(i) is int:
                for j in range(i):
                    string += "*"
            else:
                string += i
        if len(string) != len(word):
            return False

        for i in range(len(string)):
            if string[i] != "*" and string[i] != word[i]:
                return False 
        return True