class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if not arr:
            return []
        answer = []
        left = 1
        right = len(arr)

        while left < right: 
            num = max(arr[left: right])
            print(arr[left:right])
            answer.append(num)
            left += 1
        answer.append(-1)
        return answer