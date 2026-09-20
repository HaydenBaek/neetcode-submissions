class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        curr_sum = 0
        answer = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target and left <= right:
                curr_sum -= nums[left]
                answer = min(answer, right - left + 1)
                left += 1
                
            print(curr_sum)
        return answer if answer != float('inf') else 0