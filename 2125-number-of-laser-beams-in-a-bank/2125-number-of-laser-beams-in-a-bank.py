class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        num = 0
        ans =  0
        for i in range(len(bank)):
            newnum = bank[i].count("1")

            if newnum != 0 and num != 0:
                ans += newnum * num

                num = newnum
            elif newnum != 0:
                num = newnum
        
        return ans

            
