# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):

        self.ans = 0
        self.cnt = 0
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            self.cnt += 1
            if root:
                # print(self.cnt)
                helper(root.left)
                if self.cnt == 2:
                    if root.left:
                        print(root.left.val)
                        self.ans += root.left.val
                helper(root.right)
                if self.cnt == 2:
                    if root.right:
                        print(root.right.val)
                        self.ans += root.right.val
            self.cnt -= 1
            # print(self.cnt)

            return self.ans

        def traverse(root):
            if root:
                if root.val % 2 == 0:
                    helper(root)
                traverse(root.left)
                traverse(root.right)
            
            return self.ans
        
        return traverse(root)
                    
