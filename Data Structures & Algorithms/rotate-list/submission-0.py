# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # handle the edge case of head being null
        if not head:
            return head

        # find the tail and the length
        tail, length = head, 1

        while tail.next:
            tail = tail.next
            length += 1
        
        # now we have access to the tail and we have the length of the linkedlist
        # calculate how much nodes we have to rotate
        k %= length # -> gives us the remainder

        # @edgecase
        # handle if k == length of the list, no rotation required
        if k == 0: 
            return head
        
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        
        # save the new_head
        new_head = cur.next
        # cut ties with the new head because if not we get a loop when we change
        # the next ptr of new_head
        cur.next = None
        tail.next = head
        return new_head

