class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root, 0)
    def dfs(self, word, current, index):

        if index == len(word):
            return current.isEndOfWord
        
        c = word[index]

        if c != '.':
            if c not in current.children:
                return False
            return self.dfs(word, current.children[c], index + 1)
 
        for _, val in current.children.items():
            if self.dfs(word, val, index + 1):
                return True
        
        return False