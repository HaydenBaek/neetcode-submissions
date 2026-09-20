class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
 
        stack = []
        for token in tokens:
            if token == "+":
                answer = int(stack.pop()) + int(stack.pop())
                stack.append(answer)
            elif token == "-":
                first, second = stack.pop(), stack.pop()
                answer = int(second) - int(first)
                stack.append(answer)
            elif token == "*":
                answer = int(stack.pop()) * int(stack.pop())
                stack.append(answer)
            elif token == "/":
                first, second = int(stack.pop()), int(stack.pop())
                answer = (int(second/first))
                stack.append(answer)
            else:
                stack.append(token)
        return int(stack[0])