class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter

        maxa = float("-inf")
        n = len(s)
        dicts = Counter()
        l = 0
        for r in range(n):
            dicts[s[r]] += 1

            while (r - l + 1 ) - max(dicts.values()) > k:
                dicts[s[l]] -= 1
                l += 1
            
            maxa = max(maxa, r - l + 1)
        
        return maxa if maxa != float("-inf") else 0
