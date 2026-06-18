# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, cur_sum):
            if not root:
                return False
            cur_sum += root.val
            if root and not root.left and not root.right and cur_sum == targetSum:
                return True
           
            

            return dfs(root.left, cur_sum) or dfs(root.right, cur_sum)
        
        return dfs(root, 0)

        