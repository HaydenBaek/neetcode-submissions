class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        seen = set(arr)
        counter = 0
        for i in arr:
            if i + 1 in seen:
                counter += 1
        return counter