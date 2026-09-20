class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        rule = {'}':'{',']':'[',')':'('}
        
        for i in s:

            if i in rule:
                
                if stack and stack[-1] == rule[i]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(i)
        if stack:
            return False
        return True

