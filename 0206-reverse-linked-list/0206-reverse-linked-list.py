# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevn = None
        nextn = None

        temp = head

        while temp:
            nextn = temp.next
            temp.next = prevn
            
            prevn = temp
            temp = nextn
        
        return prevn


