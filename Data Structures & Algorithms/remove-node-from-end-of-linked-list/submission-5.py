# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        total = 1

        while curr.next:
            total += 1
            curr = curr.next
        if total == 1:
            return None
            
        k = total - n

        if k == 0:
            return head.next

        curr = head
        while k > 1:
            k -= 1
            curr = curr.next
        
        temp = curr.next.next
        curr.next = temp

        return head
        
    
