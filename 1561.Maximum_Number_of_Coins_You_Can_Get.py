class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        lenp = len(piles)
        maxr = lenp - (lenp//3)

        sumn = 0
        for i in range(1, maxr + 1, 2):
            sumn += piles[i]
        return sumn
