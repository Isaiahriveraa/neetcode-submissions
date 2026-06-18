class Node:
    def __init__(self, key: int, val: int, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key


class LRUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lookup = {}

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.remove(self.lookup[key])
            self.insert(self.lookup[key])
            return self.lookup[key].val
        return -1

    def put(self, key, val):
        if key in self.lookup:
            # need to update and remove it
            self.remove(self.lookup[key])
        self.lookup[key] = Node(key, val)
        self.insert(self.lookup[key])        

        if len(self.lookup) > self.cap:
            lru = (self.head.next) # we want the node.
            self.remove(lru)
            del self.lookup[lru.key] # that way we maintain the size of the double linked list

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):  # insert @ tail
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node  # adding new node to MRU
        node.next, node.prev = nxt, prev 


        


        
