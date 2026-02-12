class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        from collections import Counter
        freqres = Counter()
        res = []

        for eachlist in responses:
            for word in set(eachlist):
                freqres[word] += 1
        

        sortedfreqres = dict(sorted(freqres.items(), key=lambda item:item[1], reverse = True) )
        
        for key, value in sortedfreqres.items():
            highest = value
            break

        for key, value in sortedfreqres.items():
            if value == highest:
                res.append(key)
            else:
                break
        res.sort()
        return res[0]
        
        
            

