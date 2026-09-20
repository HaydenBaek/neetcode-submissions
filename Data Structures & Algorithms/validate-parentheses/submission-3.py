class Solution:
    def isValid(self, s: str) -> bool:
        
        closed_open_map = {')': '(', '}': '{', ']': '['}

        stack = []

        for c in s:
            if c in closed_open_map:
                if stack and stack[-1] == closed_open_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False