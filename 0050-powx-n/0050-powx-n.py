class Solution:

    def myPow(self, x: float, n: int) -> float:

        def dopower(x, n):
            if n < 0:
                return 1 / dopower(x, abs(n))
            
            if n == 0:
                return 1
            
            y = dopower(x, n//2)
            y *= y
            if n % 2:  
                y *= x
                
            return y
        return dopower(x,n)