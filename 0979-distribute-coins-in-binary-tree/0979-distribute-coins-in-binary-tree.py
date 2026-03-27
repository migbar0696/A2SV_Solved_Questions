# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def cntnode(root):
            if not root:
                return (0, 0)
            if root:
                left, leftcoin =  cntnode(root.left)
                right, rightcoin =  cntnode(root.right)


                ans =  left + right + 1
                coinsum = leftcoin + rightcoin + root.val
                self.res += abs(ans - coinsum)
                return (ans, coinsum)
        cntnode(root)
        return self.res