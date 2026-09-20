class MyStack:

    def __init__(self):
        self.stack_queue = deque()

    def push(self, x: int) -> None:
        self.stack_queue.append(x)

    def pop(self) -> int:
        temp = []
        while len(self.stack_queue) > 1:
            temp.append(self.stack_queue.popleft())
        last_element = self.stack_queue.popleft()

        for num in temp:
            self.stack_queue.append(num)
        
        return last_element

    def top(self) -> int:
        temp = []
        while len(self.stack_queue) > 1:
            temp.append(self.stack_queue.popleft())
        last_element = self.stack_queue.popleft()

        for num in temp:
            self.stack_queue.append(num)
        self.stack_queue.append(last_element)
        return last_element    

    def empty(self) -> bool:
        return False if self.stack_queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()