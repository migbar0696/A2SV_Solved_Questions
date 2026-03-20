# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr1 = []
        self.arr2 = []
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(root, arr):
            if root:
                traverse(root.left, arr)
                arr.append("")
                arr.append(root.val)
                traverse(root.right, arr)
                arr.append("")

                
            return arr
        
        return traverse(p, self.arr1) == traverse(q, self.arr2)