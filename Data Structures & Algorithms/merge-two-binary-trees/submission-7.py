# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # so lets merge into root1

        def dfs(one, two):
            
            if not one:
                return two
            
            if not two: 
                return one
            
            # okay combine into one
            one.val += two.val
            one.left = dfs(one.left, two.left)
            one.right = dfs(one.right, two.right)

            return one
        
        return dfs(root1, root2)
            
    
