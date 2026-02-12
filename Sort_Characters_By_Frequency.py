class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

        freql = Counter(s)
        res = []

        sortedfreql = dict(sorted(freql.items(), key=lambda item:item[1], reverse = True))

        for key, value in sortedfreql.items():
            res.append(key * value)
        
        return "".join(res)
      
