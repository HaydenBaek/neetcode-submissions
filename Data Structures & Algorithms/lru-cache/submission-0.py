class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
    def moveToEnd():
        before
     
class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.right = self.tail
        self.tail.left = self.head
    
    #remove from list
    def remove(self, node):
        left = node.left
        right = node.right
        left.right = right
        right.left = left
    #insert at right
    def insert(self, node):
        
        prev = self.tail.left
        prev.right = node
        node.left = prev
        self.tail.left = node
        node.right = self.tail
        
    
    def get(self, key: int) -> int:

        if key in self.cache:
            #removing it so that it goes to the end of the linked list
            self.remove(self.cache[key])
            #inserting it again, now at the end (most recently used)
            self.insert(self.cache[key])
            #returning the value (value didn't change when we removed)
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove and delete the Least Recently Used (the start)
            lru = self.head.right
            self.remove(lru)
            del self.cache[lru.key]

