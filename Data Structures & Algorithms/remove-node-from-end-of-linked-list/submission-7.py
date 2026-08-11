# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        slow = fast = dummy

        dummy.next = head

        # establishing the gap between slow and fast
        for _ in range(n + 1):
            fast = fast.next 
        
        while fast:
            slow = slow.next
            fast = fast.next 

        # now that we landed in the pos before the node that we are supposed to remove
        # we want to make the next pointer point to the next next that way
        # we remove the node
        slow.next = slow.next.next

        # handles the edge case of removing head as well
        return dummy.next
        