class Solution:
    def checkEqual(self, a, b) -> bool:
        from collections import Counter
        return Counter(a) == Counter(b)
