# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            
            cur = cur.right
        
        return -1
        

    ''' 
        ans = []
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
    
        dfs(root)
        return ans[k - 1] 
    ''' 





        
            
