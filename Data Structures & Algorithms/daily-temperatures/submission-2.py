class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):

            if stack and stack[-1][0] >= temperatures[i]:
                stack.append((temperatures[i], i))
            else:

                while stack and stack[-1][0] < temperatures[i]:
                    temp, index = stack.pop()
                    result[index] = i - index
                stack.append((temperatures[i], i))
        return result
                    