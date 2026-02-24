class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))

        while l <= r:
            if l * l + r * r > c:
                r -= 1
            elif l * l + r * r < c:
                l += 1
            else:
                return True
        
        return False