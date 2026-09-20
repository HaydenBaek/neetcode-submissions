class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        
        pairs = self.storage[key]
        left = 0
        right = len(pairs) - 1
        answer = ""
        while left <= right:
            mid = (left + right) // 2
            current = pairs[mid][0]
            if current == timestamp:
                return pairs[mid][1]
            elif current > timestamp:
                right = mid - 1
            else:
                answer = pairs[mid][1] 
                left = mid + 1
        return answer


        