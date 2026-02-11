class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        from collections import Counter
        changed.sort()
        n = len(changed)
        dictch = Counter(changed)
        res = []

        if n % 2:
            return []
        
        for num in changed:
            if num == 0 and num in dictch and dictch[num] >= 2:
                dictch[num] -= 2
                res.append(num)
                if dictch[num] == 0:
                    del dictch[num]


            elif num in dictch and 2 * num in dictch and num != 0:
                dictch[num] -= 1
                dictch[2 * num] -= 1
                res.append(num)

                if dictch[num] == 0:
                    del dictch[num]
                
                if dictch[ 2 * num] == 0:
                    del dictch[2 * num]
            
        return res if len(res) == n //2 else []
                     



        


