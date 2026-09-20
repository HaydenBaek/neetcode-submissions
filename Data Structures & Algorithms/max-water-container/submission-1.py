class Solution:
    def maxArea(self, heights: List[int]) -> int:


        most_amount = 0

        left = 0
        right = len(heights) - 1

        while left <= right:

            width = right - left
            
            min_bar = min(heights[left],heights[right])
            most_amount = max(most_amount, width*min_bar)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return most_amount

