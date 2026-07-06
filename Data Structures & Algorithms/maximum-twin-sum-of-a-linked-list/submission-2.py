# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # whats the length of the linkedlist
        # slow and fast pointer mult slow poitner by 2 and then we have to make sure that the n is even
        
        slow, fast = head, head.next

        # find the middle of the linkedlist
        # slow will land there
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        other_half = slow.next
        slow.next = None # disconnect the other half
        # reverse the other half

        prev = None
        cur = other_half

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # prev is now head of the reversed other half

        res = 0
        # Since n is even meaning they will be the same length for each linkedlist
        # we can process them at the same time, processing the twins sum and recording it res
        while prev and head:
            res = max(prev.val + head.val, res)
            prev = prev.next
            head = head.next

        return res



            

        
