# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        dummy = head

        while l1 or l2:
            if not l1: 
                val = l2.val + carry
                l2 = l2.next
            elif not l2:
                val = l1.val + carry
                l1 = l1.next
            else:
                val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            if val >=10:
                val = val % 10
                carry = 1
            else:
                carry = 0
            dummy.next = ListNode(val)
            dummy = dummy.next
        
        if carry:
            dummy.next = ListNode(1)
        return head.next



