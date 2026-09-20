class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        answer = []

        left = 0
        right = k
        n = len(nums)
        while right < n + 1:
            answer.append(max(nums[left:right]))
            left += 1
            right += 1
        
        return answer