class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []
        
        rows, columns = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):

            if ( r < 0 or c < 0 or r >= rows or c >= columns or (r,c) in visited or heights[r][c] < prev_height):
                return
            
            visited.add((r,c))

            #exploring 4 directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(columns):
            dfs(0, c, pacific, heights[0][c]) #top row
            dfs(rows - 1, c, atlantic, heights[rows-1][c]) #bottom row
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0]) #left column
            dfs(r, columns - 1, atlantic, heights[r][columns - 1]) #right column
        
        # intersection -> cells taht both oceans can reach
        result = [[r, c] for (r,c) in pacific & atlantic]
        return result
