class Solution:
    def minCost(self, n: int) -> int:


        return n * (n - 1)//2
        
        # memo = defaultdict(int)
        # ans = 0

        # def helper(n):
        #     nonlocal ans

        #     if n <= 1:
        #         return
            
        #     if n not in memo:
        #         memo[n] = (n//2) * ceil(n/2)
            
        #     ans += memo[n]

        #     helper(n//2) 
        #     helper(ceil(n/2))
        
        # helper(n)
        # # print(memo)
        # return ans

        
