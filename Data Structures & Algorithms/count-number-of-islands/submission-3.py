class Solution:

    def dfs(self, grid, row, column):
        grid[row][column] = "0"
        lst = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]
        for row, column in lst:
            if row >= 0 and column >= 0 and row < len(grid) and column < len(grid[row]) and grid[row][column] == '1':
                self.dfs(grid, row, column)

    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == "1":
                    self.dfs(grid, row, column)
                    islands += 1
        
        return islands
        