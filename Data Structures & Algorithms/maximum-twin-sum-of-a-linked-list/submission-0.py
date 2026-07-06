# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # whats the length of the linkedlist
        # slow and fast pointer mult slow poitner by 2 and then we have to make sure that the n is even

        cur = head
        twin_list = []
        while cur:
            twin_list.append(cur.val)
            cur = cur.next
        

        res = 0
        n = len(twin_list)
        for i in range(n):
            # whats the twin
            res = max(res, twin_list[i] + twin_list[n - 1 - i]) 
        
        return res
            

        
