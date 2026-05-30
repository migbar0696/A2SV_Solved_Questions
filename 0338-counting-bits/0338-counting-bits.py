class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = defaultdict(int)
        ans = []

        for i in range(n + 1):
            
            if i not in memo:

                memo[i] = bin(i).count("1")

            ans.append(memo[i])
        
        return ans
        
