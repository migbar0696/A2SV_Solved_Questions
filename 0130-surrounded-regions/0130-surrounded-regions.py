class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """

        m = len(board)
        n = len(board[0])

        visited = [[False for i in range(n)] for j in range(m) ]

        surrounded = True

        def is_edge(r, c):
            return r == 0 or r == m - 1 or c == 0 or c == n - 1

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def dfs(r, c):
            # print(r,c)
            nonlocal surrounded
            
            visited[r][c]= True

            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for rc, cc in direction:
                nrc = r + rc
                ncc = c + cc

                if inbound(nrc, ncc) and not visited[nrc][ncc] and board[nrc][ncc] == 'O':
                    dfs(nrc, ncc)
                


        

            
        

        for i in range(m):
            for j in range(n):

                if board[i][j] == 'O' and is_edge(i, j):
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):

                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = "X"
        
                
        
                




