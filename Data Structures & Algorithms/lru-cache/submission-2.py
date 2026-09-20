class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.right = self.tail
        self.tail.left = self.head
    
    def remove(self, node):

        prev = node.left
        nxt = node.right
        prev.right = nxt
        nxt.left = prev
    
    def insert(self, node):

        prev = self.tail.left
        node.left = prev
        prev.right = node
        node.right = self.tail
        self.tail.left = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(-1, -1)
        else:
            self.remove(self.cache[key])
        self.cache[key].key = key
        self.cache[key].value = value
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.head.right
            nxt = lru.right
            self.head.right = nxt
            nxt.left = self.head
            self.remove(lru)
            del self.cache[lru.key]
            
        

