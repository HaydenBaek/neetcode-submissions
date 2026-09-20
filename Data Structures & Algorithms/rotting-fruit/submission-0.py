class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col, 0))

        maxTime = 0
        
        while q:
            r, c, time= q.popleft()
            maxTime = max(maxTime, time)

            if r + 1 < rows and grid[r + 1][c] == 1 and (r + 1, c):
                grid[r + 1][c] = grid[r][c]
                q.append((r + 1, c, time + 1))
            
            if r - 1 >= 0 and grid[r - 1][c] == 1 and (r - 1, c):
                grid[r - 1][c] = grid[r][c]
                q.append((r - 1, c, time + 1))
  
            if c - 1 >= 0 and grid[r][c - 1] == 1 and (r, c - 1):
                grid[r][c - 1] = grid[r][c]
                q.append((r, c - 1, time + 1))

            if c + 1 < cols and grid[r][c + 1] == 1 and (r, c + 1):
                grid[r][c + 1] = grid[r][c]
                q.append((r, c + 1, time + 1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return maxTime
