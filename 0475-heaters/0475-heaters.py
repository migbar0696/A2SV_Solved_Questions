class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def helper(num):
            i = -1

            for each in heaters:
                if i < len(houses) - 1 and houses[i + 1]  >= each - num :
                    lefta = -1
                    righta = len(houses)
                    while lefta + 1 < righta:
                        mida = (lefta +  righta)//2
                        # print(mida, "mid")

                        if houses[mida] <= each + num :
                            lefta = mida

                        else:
                            righta = mida
                    
                    i = lefta
            if houses[i]  >= houses[-1] and i != -1:
                return True
            
            return False
        
        left = -1
        right = 10 ** 9 + 1
        print(houses)
        print(heaters)
        print(helper(0))

        while left + 1 < right:
            mid = (left + right)//2

            if helper(mid):
                right = mid
            else:
                left = mid
            # print(left, right, ' inside')
        
        return right

