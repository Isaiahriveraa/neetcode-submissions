# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left, right, root):

            if not root:
                return True
            
            l = dfs(left, root.val, root.left) 
            r = dfs(root.val, right, root.right)

            if not (left < root.val < right):
                return False
            
            return l and r
        
        return dfs(float('-inf'), float('inf'), root)