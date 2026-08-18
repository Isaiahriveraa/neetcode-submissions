"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        clone = {}
        def dfs(head):
            if not head:
                return None

            if head in clone:
                return clone[head]
            
            # make the clone
            clone[head] = Node(head.val)

            # now we must connect all the nodes
            clone[head].next = dfs(head.next)
            clone[head].random = dfs(head.random)
        
            return clone[head]

        return dfs(head)
