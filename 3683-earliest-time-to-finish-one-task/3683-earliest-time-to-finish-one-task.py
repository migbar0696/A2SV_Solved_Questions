class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mint = float('inf')
        for each in tasks:
            mint = min(mint, each[0] + each[1])
        
        return mint