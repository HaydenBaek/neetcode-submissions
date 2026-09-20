class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def calculate_island(r, c):

            perm = 0
            if r - 1 < 0 or grid[r - 1][c] == 0:
                perm += 1
            if r + 1 >= rows or grid[r + 1][c] == 0:
                perm += 1
            if c - 1 < 0 or grid[r][c - 1] == 0:
                perm += 1
            if c + 1 >= cols or grid[r][c + 1] == 0:
                perm += 1
            
            return perm
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += calculate_island(r, c)
        
        return perimeter
