# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # we are given a bst that is sorted so we can use this to our advantage 
        # We want to do an inorder traversal left, root, right
        # we have to return the kth smallest integer
        # Contraints:
        #   we dont know the length of the bst
        #   its 1 indexed
        # [2] go left that means that thats [2, 1]
        res = []
        k -= 1
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

            return
        dfs(root)
        return res[k]
