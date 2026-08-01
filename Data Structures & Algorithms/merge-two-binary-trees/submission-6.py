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
            if one and two:
                root = TreeNode(one.val + two.val)
                root.left = dfs(one.left, two.left)
                root.right = dfs(one.right, two.right)
                return root
            elif not one:
                return two
            elif not two:
                return one
            else:
                return None
        
        return dfs(root1, root2)