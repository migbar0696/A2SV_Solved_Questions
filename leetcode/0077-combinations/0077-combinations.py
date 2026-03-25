class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        ans = []
        
        def backtrack(start, comb):

            if len(comb) == k:
                ans.append(comb.copy())
                return 

            if start > n:
                return 
            
            comb.append(start)

            backtrack(start + 1, comb)

            comb.pop()
            backtrack(start + 1, comb)
        
        backtrack(1,[])
        return ans