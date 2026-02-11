class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter

        freqs = Counter(s)
        freqt = Counter(t)

        for ch in freqs.keys():
            if freqt[ch] > freqs[ch]:
                freqs[ch] = 0
            else:
                freqs[ch] -= freqt[ch]
        
        minstep = sum(value for value in freqs.values())

        return minstep
