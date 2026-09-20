class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        stack = []

        for op in operations:
            if op == "+":
                if len(stack) > 1:
                    curr_sum = stack[-1] + stack[-2]
                    stack.append(curr_sum)
            elif op == "C":
                if stack:
                    stack.pop()
            elif op == "D":
                if stack:
                    stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
            print(stack)
        return sum(stack)
