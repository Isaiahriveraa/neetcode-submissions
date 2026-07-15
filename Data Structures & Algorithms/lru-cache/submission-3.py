class ListNode:

    def __init__(self, val, next=None, prev=None, key=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lookup = {}
        self.cap = capacity
        


    def get(self, key: int) -> int:
        # we need to access it then add it to the right of the linked list
        if key not in self.lookup:
            return -1

        node = self.remove(key) # get the node 
        self.add(key, node.val) # since we accessed it we need to add it back to the right of the linked list
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup: # if the key is already there we need to update the val
            self.remove(key)
            self.cap += 1

        self.add(key, value)
        self.cap -= 1

        if self.cap < 0:
            self.remove(self.head.next.key)
            self.cap += 1


        
    def add(self, key, val):

        # make the node
        new_node = ListNode(val, None, None, key)

        # we already have this value so lets remove it then add it
        if key in self.lookup: 
            self.remove(key)
        
        self.lookup[key] = new_node
        
        # add to the right of the list
  
        prev_last_node = self.tail.prev

        # replace it

        prev_last_node.next = new_node
        new_node.prev = prev_last_node
        new_node.next = self.tail
        self.tail.prev = new_node
    


    def remove(self, key):

        # remove it from the lookup
        # remove it from the linkedlist

        cur = self.lookup[key]

        left_node = cur.prev
        right_node = cur.next

        left_node.next = right_node
        right_node.prev = left_node

        del self.lookup[key]

        return cur