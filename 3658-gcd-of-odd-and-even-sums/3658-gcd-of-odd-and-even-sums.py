class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumo = 0
        sume = 0
        for i in range(1, 2 * n + 1):
            if i % 2:
                sumo += i
            else:
                sume += i
        
    
        return math.gcd(sumo, sume)
        