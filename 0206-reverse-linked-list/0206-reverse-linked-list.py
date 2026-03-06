# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode(5001)
        new_head = dummynode

        while head:
            temp = head
            
            head = head.next

            temp.next = dummynode.next
            dummynode.next = temp
        
        return new_head.next
        

