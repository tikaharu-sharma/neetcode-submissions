class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    #doubly linked list

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        #left-least recent, right-most recent
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):  #insert from right
        self.right.prev.next = node
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev = node

    def remove(self, node):  #remove the node
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]








        
