class Solution:
    def isHappy(self, n: int) -> bool:
        setn = {n}
        if n == 1:
            return True
        while n != 1:
            setn.add(n)
            n = sum(int(i) * int(i)  for i in str(n))
            
            if n in setn:
                return False
        return True



            
        
