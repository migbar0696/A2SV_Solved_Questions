class Solution:
    def findValidPair(self, s: str) -> str:
        from collections import Counter

        freqs = Counter(s)
        n = len(s)

        for i in range(n - 1):
    
            if s[i] != s[i + 1] and int(s[i]) == freqs[s[i]] and int(s[i + 1]) == freqs[s[i  + 1]]:
                return f"{s[i]}{s[i + 1]}"
        
        return ""
