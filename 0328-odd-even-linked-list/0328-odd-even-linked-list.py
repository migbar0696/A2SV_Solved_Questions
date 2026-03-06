# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if not head or not head.next or not head.next.next:
            return head

        flag = True
        firsteven = head.next
        lastodd = None

        while temp.next:
            curr = temp
            nextn = temp.next

            curr.next = curr.next.next
            temp = nextn
            
        lasto = head
        while lasto:
            lastodd = lasto
            lasto = lasto.next
        
        lastodd.next = firsteven
        
        return head