# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.temp = []
        self.sumn = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(root):
            if root:
                self.sumn += root.val
                self.temp.append(root.val)

                helper(root.left)
                helper(root.right)

                if not root.right and not root.left and self.sumn == targetSum:
                    self.ans.append(self.temp.copy())

                self.sumn -= root.val
                self.temp.pop()
            return self.ans
        
        return helper(root)