class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        cnt5 = 0
        cnt10 = 0
        cnt20 = 0


        for ind, bill in enumerate(bills):

            if bill == 5:
                cnt5 += 1
            elif bill == 10:
                cnt10 += 1
                cnt5 -= 1
            else:
                if cnt10 == 0:
                    cnt5 -= 3
                elif cnt10 > 0:
                    cnt5 -= 1
                    cnt10 -= 1

            print(cnt5, cnt10)
            if cnt5 < 0 or cnt10 < 0 :
                return False
        
        return True
