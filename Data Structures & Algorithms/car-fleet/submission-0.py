class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        n = len(position)

        for i in range(n):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        
        cars.sort(reverse=True)

        stack = []

        for pos, time in cars:

            if stack and time <= stack[-1]:
                continue
            
            stack.append(time)
        
        return len(stack)