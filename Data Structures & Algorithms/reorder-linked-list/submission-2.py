# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
    
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None

        prev = None
        curr = temp
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        main = head
        while prev:
            temp1 = main.next
            temp2 = prev.next
            main.next = prev
            prev.next = temp1
            main = temp1
            prev = temp2