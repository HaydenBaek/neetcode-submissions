class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        rows = len(board)
        cols = len(board[0])

        q = deque()

        #only going through the 1st and last col
        for r in range(rows):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][cols - 1] == "O":
                q.append((r, cols - 1))
            
        #goign through the frist and last row
        for c in range(cols):
            if board[0][c] == "O":
                q.append((0, c))
            if board[rows - 1][c] == "O":
                q.append((rows - 1, c))
        

        #bfs now
        while q:
            r, c = q.popleft()

            if board[r][c] != "O":
                continue
            board[r][c] = "T" #temp marker

            if r + 1 < rows and board[r + 1][c] == "O":
                q.append((r + 1, c))
            if r - 1 >= 0 and board[r - 1][c] == "O":
                q.append((r - 1, c))
            if c - 1 >= 0 and board[r][c - 1] == "O":
                q.append((r, c - 1))
            if c + 1 < cols and board[r][c + 1] == "O":
                q.append((r, c + 1))

        
        for r1 in range(rows):
            for c1 in range(cols):
                if board[r1][c1] == "T":
                    board[r1][c1] = "O"
                    continue
                board[r1][c1] = "X"












