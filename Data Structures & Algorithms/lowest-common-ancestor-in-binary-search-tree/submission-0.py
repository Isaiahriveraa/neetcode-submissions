# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # lowest Common Ancestor
        # p and q
        cur = root 
        while cur:
            print(cur.val)
            if p.val < cur.val and q.val < cur.val: # both greater go right # if the p.val < root and so is q.val then go left
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                break
        return cur