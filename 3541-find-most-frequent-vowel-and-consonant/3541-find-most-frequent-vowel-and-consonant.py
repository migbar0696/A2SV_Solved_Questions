class Solution:
    def maxFreqSum(self, s: str) -> int:
        freqe = Counter(s)

        maxv = 0
        maxc = 0

        for key, value in freqe.items():
            if key in ["a", "i", "o", "u", "e"]:
                maxv = max(maxv, value)
            else:
                maxc = max(maxc, value)
        
        return maxc + maxv