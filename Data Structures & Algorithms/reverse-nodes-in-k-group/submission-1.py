# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            last = self.knode(groupPrev, k)
            if not last:
                break
            groupNext = last.next

            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            oldGroupStart = groupPrev.next
            groupPrev.next = last
            groupPrev = oldGroupStart

        return dummy.next
            

    def knode(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node    

    



