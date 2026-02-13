class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rowl = len(grid)
        coll = len(grid[0])
        cnt = 0
        for i in range(rowl):
            for j in range(coll):
                if grid[i][j] < 0:
                    cnt += 1
        
        return cnt
