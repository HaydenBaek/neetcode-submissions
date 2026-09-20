class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0
        
        def dfs(r, c, count):

            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or
                (r, c) in visited or
                grid[r][c] == 0):
                return count
            
            visited.add((r,c))

            return 1 + dfs(r + 1, c, count) + dfs(r - 1, c, count) + dfs(r, c + 1, count) + dfs(r, c - 1, count)

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    count = 0
                    maxArea = max(maxArea, dfs(row, col, count))

        
        return maxArea