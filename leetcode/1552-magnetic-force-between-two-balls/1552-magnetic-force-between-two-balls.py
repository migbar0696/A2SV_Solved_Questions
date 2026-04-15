class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        print(position)

        def helper(num):
            pos = 0
            newm = m - 1
            while newm  > 0:
                newpos = bisect_left(position, position[pos] + num)
                print(newpos)
                if  newpos < len(position):
                    pos = newpos
                else:
                    return False
                
                newm -= 1
            return True
        
        left = 0
        right = 10 ** 9
        # print(helper(4))
        while left + 1 < right:
            
            mid = left + (right - left)//2

            if helper(mid):
                left = mid
            else:
                right = mid
        
        return left