# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def minmove(root):
            if not root:
                return (0, 0)
            if root:
                left, leftcoin =  minmove(root.left)
                right, rightcoin =  minmove(root.right)


                ans =  left + right + 1
                coinsum = leftcoin + rightcoin + root.val
                self.res += abs(ans - coinsum)
                
                return (ans, coinsum)
        minmove(root)
        return self.res