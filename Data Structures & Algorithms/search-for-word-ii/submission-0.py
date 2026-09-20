class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
    
    def addWord(self, word):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isEndOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        rows = len(board)
        cols = len(board[0])
        result = set()
        visited = set()

        def dfs(r, c, node, word):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or board[r][c] not in node.children):
                return 
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEndOfWord:
                result.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(result)