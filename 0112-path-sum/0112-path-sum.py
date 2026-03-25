# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sumn = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.target = targetSum
        def helper(root):
            if root:
                self.sumn += root.val
                pos1 = helper(root.left)
                pos2 = helper(root.right)
                
                if not root.right and not root.left and self.sumn == self.target:
                    return True
    
                self.sumn -= root.val

                return pos1 or pos2

            
            return False
        return helper(root)
