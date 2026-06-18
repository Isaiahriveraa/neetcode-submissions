# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use bfs left, root, right
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            length = len(q)
            sub_list = []
            for _ in range(length):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                sub_list.append(cur.val)
            res.append(sub_list)
            
        return res
                