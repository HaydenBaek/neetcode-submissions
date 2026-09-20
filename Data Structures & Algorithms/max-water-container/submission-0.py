class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        width = len(heights) - 1
        total = 0

        while left < right:

            smallBar = min(heights[left], heights[right])

            total = max(total, smallBar * width)

            if heights[left] > heights[right]:
                right -=1
            else:
                left += 1
            width -= 1

        return total
        

        