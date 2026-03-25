# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sumn = 0
        self.cnt = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
            self.target = targetSum
            def helper(root):
                if root:
                    self.sumn += root.val
                    if  self.sumn == self.target:
                        self.cnt += 1
                    pos1 = helper(root.left)
                    pos2 = helper(root.right)
                    
                    self.sumn -= root.val
        

                    return self.cnt

                
                return self.cnt
            return helper(root)

        if root:
            self.sumn = 0
            hasPathSum(root,targetSum)
            self.pathSum(root.left, targetSum)
            self.pathSum(root.right, targetSum)


        return self.cnt  if root else 0
        