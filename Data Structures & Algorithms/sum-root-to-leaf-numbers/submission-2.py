# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        stack = [(root, 0)]
        res = 0

        while stack:
            cur_root, cur = stack.pop()
            if not cur_root:
                return 0
            
            # want to add the cur number
            cur = cur * 10 + cur_root.val
            print(cur)
            # now we must add the cur if the root is a leaf node
            if not cur_root.right and not cur_root.left:
                res += cur
                
            
            if cur_root.left:
                stack.append((cur_root.left, cur))
            if cur_root.right:
                stack.append((cur_root.right, cur))
        
        return res