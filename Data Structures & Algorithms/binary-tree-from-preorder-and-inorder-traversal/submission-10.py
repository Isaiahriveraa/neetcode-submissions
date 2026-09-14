# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        num_to_index = { num: index for index, num in enumerate(inorder) } # create a hashmap that way we can look for the index easily
        root_index = 0

        def dfs(left, right):
            nonlocal root_index 

            if left > right:
                return None
            root_val = preorder[root_index]
            root = TreeNode(root_val)
            mid = num_to_index[root_val]
            root_index += 1

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root
        
        return dfs(0, len(preorder) - 1)

            

