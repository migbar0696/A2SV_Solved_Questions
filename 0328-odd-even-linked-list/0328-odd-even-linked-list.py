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
        firsteven = None
        lastodd = None
        i = 1
        while temp.next:
            if i % 2:
                lastodd = temp
            elif temp.next:
                lastodd = temp.next
            i += 1
            curr = temp
            nextn = temp.next

            curr.next = curr.next.next
            temp = nextn

            if flag:
                firsteven = temp
                flag = False
        
        lastodd.next = firsteven
        
        return head