class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        answer = [0] * len(temperatures)
        for i, t in enumerate(temperatures):

            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                answer[index] = i - index
            stack.append((i,t))
        
        return answer