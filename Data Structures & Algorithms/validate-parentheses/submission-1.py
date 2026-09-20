class Solution:
    def isValid(self, s: str) -> bool:

        rule = {'}':'{', ']':'[', ')':'('}

        stack = []

        for i in s:

            if i in rule:
                if not stack or stack[-1] != rule[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        return True



        