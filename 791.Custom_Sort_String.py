class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        freqs = Counter(s)
        res = []

        for char in order:
            for i in range(freqs[char]):
                res.append(char)
            freqs[char] = 0

        for lchar in freqs.keys():
            for j in range(freqs[lchar]):
                res.append(lchar)
        
        return "".join(res)

