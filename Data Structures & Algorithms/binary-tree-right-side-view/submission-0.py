# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # we want to keep track of only the right nodes so what do we do
        # we want to do level order traversal
        # that means that we want to add all the nodes in the current row and then we 
        # want to 
        """
        deque = [1]
        pop -> 1
        does 1 have a left? yes add it 
        deque = [2] 
        does it have a right? yes add it
        deque = [2, 3]
        now the len(q) == if i - 1 == len(q): meaning that we are on the last node then we can append it to the res 
                                     [1]  
                                [2]       [3]  
                                    [4]         [5]


        """
        if not root:
            return []

        q = deque([root])
        res = []

        while q:

            len_q = len(q)

            for i in range(1,len_q + 1):
                cur = q.popleft()
                
                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)
                
                if i == len_q:
                    res.append(cur.val)
            
        return res
                
