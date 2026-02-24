class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        maxi = float("-inf")
        n = len(s)
        sumi = 0
        res = []
        for i in range(n):
            maxi = max(maxi, s.rindex(s[i]))
            
            if i == maxi:
                res.append(i + 1 - sumi)
                sumi = i + 1
        
        return res
 
