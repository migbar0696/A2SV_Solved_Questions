class Solution:
    def myPow(self, x: float, n: int) -> float:
        mod = (10 **9) + 7
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        
        if n == 0:
            return 1
        
        y =self.myPow(x, n//2) 
        y *= y%mod
        if n % 2:  
            y *= x%mod
            
        return y %mod

    def countGoodNumbers(self, n: int) -> int:
        # print(ceil(n / 2) , (n // 2 ) )
        mod = (self.myPow(10, 9)) + 7
        return (self.myPow(5, ceil(n/2)) * self.myPow(4, n//2) ) % mod