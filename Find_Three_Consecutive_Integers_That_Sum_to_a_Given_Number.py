class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res = []
        if(num - 3) % 3 == 0:
            n = (num - 3 )// 3
            res.append(n)
            res.append(n + 1)
            res.append(n + 2)
            return res
        
        return res
        
