class Solution:

    def myPow(self, x: float, n: int) -> float:
        self.pown = x

        def dopower(x, n):
            if n % 2 ==  0:
                if n < 0:
                    if n == - 1:
                        return 1 / self.pown
                if n == 0:
                    return 1
                    
                    y = dopower(x, n / 2)
                    y *= y
                    return y
                    
                else:
                    if n == 1:
                        return x
                    
                    if n == 0:
                        return 1
                    
                    y = dopower(x, n / 2)
                    y *= y
                    return y
            else:
                if n < 0:
                    if n == - 1:
                        return 1 / self.pown
                    if n == 0:
                        return 1
                    
                    return dopower(x, n //2) * dopower(x, ceil(n / 2))
                    
                else:
                    if n == 1:
                        return x
                    if n == 0:
                        return 1
                    
                    return dopower(x, n //2) * dopower(x, ceil(n / 2))


        return dopower(x, n)

        
        