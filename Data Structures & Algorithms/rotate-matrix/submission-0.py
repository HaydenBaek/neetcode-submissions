class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        

        #tranpose

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(r + 1,cols):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        
        #reflection
        for r in range(rows):
            left = 0
            right = len(matrix) - 1

            while left < right:
                temp = matrix[r][right]
                matrix[r][right] = matrix[r][left]
                matrix[r][left] = temp
                left += 1
                right -= 1
