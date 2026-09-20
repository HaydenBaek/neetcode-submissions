class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        result = [0] * len(temperatures)

        indices = []

        for i in range(len(temperatures)):

            while indices and temperatures[i] > temperatures[indices[-1]]:
                previous_day = indices.pop()
                result[previous_day] = i - previous_day
            indices.append(i)
        return result 