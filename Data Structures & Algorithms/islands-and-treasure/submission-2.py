class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        while q:
            r, c = q.popleft()

            if r + 1 < rows and grid[r + 1][c] == 2147483647:
                grid[r + 1][c] = grid[r][c] + 1
                q.append((r + 1, c))
            
            if r - 1 >= 0 and grid[r - 1][c] == 2147483647:
                grid[r - 1][c] = grid[r][c] + 1
                q.append((r - 1, c))
            
            if c - 1 >= 0 and grid[r][c - 1] == 2147483647:
                grid[r][c - 1] = grid[r][c] + 1
                q.append((r, c - 1))
            
            if c + 1 < cols and grid[r][c + 1] == 2147483647:
                grid[r][c + 1] = grid[r][c] + 1
                q.append((r, c + 1))