class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])

        zeros = set()

        def turnZeros(r, c):

            #turn cols to zero
            for col in range(cols):
                matrix[r][col] = 0
            
            #turn rows into zero
            for row in range(rows):
                matrix[row][c] = 0


        for r in range(rows):
            for c in range(cols):

                if matrix[r][c] == 0:
                    zeros.add((r, c))
        
        for r in range(rows):
            for c in range(cols):

                if (r,c) in zeros:
                    turnZeros(r, c)
               
        


