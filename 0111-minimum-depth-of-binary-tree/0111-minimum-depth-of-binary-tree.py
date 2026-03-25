# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min = float("inf")
        self.cnt = 0
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.cnt += 1
        if root:
            self.minDepth(root.left)
            self.minDepth(root.right)

            if not root.left and not root.right:
                self.min = min(self.min, self.cnt)
        self.cnt -= 1

        return self.min if self.min != float("inf") else 0
            