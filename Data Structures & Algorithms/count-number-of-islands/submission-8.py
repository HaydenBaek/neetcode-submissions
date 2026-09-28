class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        islands = 0
        def markIsland(row, col):
            grid[row][col] = "0"
            if row - 1 >= 0 and grid[row - 1][col] == "1": 
                markIsland(row - 1, col)
            if row + 1 < len(grid) and grid[row + 1][col] == "1":
                markIsland(row + 1, col)
            if col - 1 >= 0 and grid[row][col - 1] == "1":
                markIsland(row, col - 1)
            if col + 1 < len(grid[row]) and grid[row][col + 1] == "1":
                markIsland(row, col + 1)   
            

        #wait... is that the strat.....? 
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1": 
                    markIsland(r, c)
                   
                    islands += 1
        return islands