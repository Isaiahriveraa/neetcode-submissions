# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        0,1,2,3,4,5,6
        
        use fast and slow pointer
        """
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec_half = slow.next
        slow.next = None # disconnect the second half
        
        #reverse the 2nd half
        prev = None
        while sec_half:
            tmp = sec_half.next # save the nxt ptr
            sec_half.next = prev
            prev = sec_half # we need to make the prev point to the cur
            sec_half = tmp
        
        # now prev is head head of the reversed list now we must merge the 2
        
        cur = head
        while prev:
            tmp = cur.next # save the pointer 4
            cur.next = prev # 8
            prev = prev.next # 6
            cur = cur.next
            cur.next = tmp
            cur = tmp # 2->8->

            
        
            

