class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        def dfs(grid,visited, row, col ):
            direction = [(0, 1), (-1, 0), (1, 0 ), (0, -1)]
            # print(row, col)
            visited[row][col] = True
            if grid[row][col] == '1':
                for rowc, colc in direction:
                    new_row = row + rowc
                    new_col = col + colc

                    if inbound(new_row, new_col) and not visited[new_row][ new_col] and grid[new_row][ new_col] == '1':
                        # print(new_row, new_col)
                        dfs(grid, visited, new_row, new_col)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    cnt += 1
                    dfs(grid, visited, i, j)
                    # print(visited)
                # print(grid[i][j])

        return cnt
        

        
