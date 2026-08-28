# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorder_index = 0
        # make a hashmap of inorder and map the val -> index (how we cal the mid)
        val_index_inorder = { num: i for i, num in enumerate(inorder) } # num -> index

        # we can use the mid to split the tree on the left and the right of the root (mid)
        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_val = preorder[preorder_index]
            # now that we used this root we must increment to prevent using it twice
            preorder_index += 1
            root = TreeNode(root_val)
            mid = val_index_inorder[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
        return build(0, len(preorder) - 1)
        
