class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def cntday(minw):

            sumn = 0

            if minw < sumn:
                return False
            
            l = 0
            cnt = 0
            for r in range( len(weights)):

                sumn += weights[r]

                if weights[r] > minw:
                    return False

                if sumn > minw:
                    cnt += 1

                    sumn = weights[r]
            
            return True if cnt + 1 <= days else False
        
        left = 0 

        right = sum(weights)

        while left + 1 < right:

            mid = (left + right)//2

            if not cntday(mid) :
                
                left = mid
            else:
                right = mid
        
        return right
