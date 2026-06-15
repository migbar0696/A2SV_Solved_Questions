class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        sumn = 0
        for i in str(n):
            sumn += int(i)
        
        return sumn