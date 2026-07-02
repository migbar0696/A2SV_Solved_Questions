class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                max1 = max(grid[r])
                max2 = grid[0][c]
                for row in grid:
                    max2 = max(max2, row[c])
                
                ans +=  min(max1, max2) - grid[r][c] 
        
        return ans
