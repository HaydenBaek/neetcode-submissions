class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * len(nums)
        result = []
        def backtrack(path):
            if len(path) == n:
                result.append(path.copy())
                return
            
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
            
        backtrack([])
        return result
