class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLUMNS = len(board[0])
        path = set()

        def dfs(row, column, currentChar):
            if currentChar == len(word):
                return True
            if (row < 0 or column < 0 or
                row >= ROWS or column >= COLUMNS or
                word[currentChar] != board[row][column] or
                (row, column) in path):
                return False
            
            path.add((row, column))
            result = (dfs(row + 1, column, currentChar + 1) or
                    dfs(row - 1, column, currentChar + 1) or
                    dfs(row, column + 1, currentChar + 1) or
                    dfs(row, column - 1, currentChar + 1))
            path.remove((row, column))
            return result
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r, c, 0): return True
        
        return False
        