class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def helper(num):
            cnt = 0
            for each in candies:
                cnt += each // num
            
            if cnt >= k:
                return True
            
            return False
        
        left = 0
        right = max(candies) + 1
        while left + 1 < right:
            mid = left + (right - left)//2
            if helper(mid):
                left = mid
            else:
                right = mid
                print(mid, 'midr')
        
        return left