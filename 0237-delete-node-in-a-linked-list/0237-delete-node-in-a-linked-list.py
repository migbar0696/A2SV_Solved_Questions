# Definition for singly-linked list.

# class ListNode:
#     def __ init__(self, x):
#         self.val = x
#         self.next = None
        

class Solution:

    def deleteNode(self, node):
        self.node = node
        temp = self.node
        while temp.next:
            temp.val = temp.next.val
            prev = temp
            temp = temp.next
        
        prev.next = None
            
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        