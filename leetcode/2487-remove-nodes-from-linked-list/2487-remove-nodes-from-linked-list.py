# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prevn = None
        nextn = None

        temp = head
        while temp:
            nextn = temp.next
            temp.next = prevn
            prevn = temp
            temp = nextn
            # print(prevn)
        
        

        temp1 = prevn
        temp2 = prevn
        while temp1.next:
            if temp2.val <= temp1.next.val:
                temp2.next = temp1.next
                temp2 = temp1.next
    
            temp1 = temp1.next
        temp2.next = None
        
        prevn1 = None
        nextn1 = None

        temp = prevn
        while temp:
            nextn1 = temp.next
            temp.next = prevn1
            prevn1 = temp
            temp = nextn1
        
        return prevn1
            

        
            