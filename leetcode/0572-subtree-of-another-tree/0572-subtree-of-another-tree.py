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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse(root, arr):
            if root:
                arr.append(f"({root.val})")
                traverse(root.left, arr)
                arr.append("-")
                traverse(root.right, arr)
                arr.append("-")
                
            return arr
        return "".join(str(i) for i in traverse(subRoot, self.arr2)) in "".join(str(j) for j in traverse(root, self.arr1))