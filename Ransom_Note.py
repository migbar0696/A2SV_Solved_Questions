class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        freqr = Counter(ransomNote)
        freqm = Counter(magazine)

        if all(freqr[key] <= freqm[key] for key in freqr.keys()):
            return True
        
        return False
