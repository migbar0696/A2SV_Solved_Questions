class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """

        m = len(board)
        n = len(board[0])

        visited = [[[False, 0] for i in range(n)] for j in range(m) ]

        surrounded = True

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def dfscheck(r, c):
            # print(r,c)
            nonlocal surrounded
            
            visited[r][c][0] = True

            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for rc, cc in direction:
                nrc = r + rc
                ncc = c + cc

                if inbound(nrc, ncc) and not visited[nrc][ncc][0] and board[nrc][ncc] == 'O':
                    dfscheck(nrc, ncc)
                
                elif not inbound(nrc, ncc):
                    # print(nrc, ncc)
                    surrounded = False
        

        def dfsmarker(r, c):


            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            board[r][c] = "X"

            for rc, cc in direction:
                nrc = r + rc
                ncc = c + cc

                if inbound(nrc, ncc) and board[nrc][ncc] == 'O':
                    dfsmarker(nrc, ncc)
            
        def dfsassure(r, c):


            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            visited[r][c][1] = 1 

            for rc, cc in direction:
                nrc = r + rc
                ncc = c + cc

                if inbound(nrc, ncc) and board[nrc][ncc] == 'O' and visited[nrc][ncc][1] != 1:
                    dfsassure(nrc, ncc)
        

        for i in range(m):
            for j in range(n):
                # print(i, j)
                # print(board[i][j])
                if  board[i][j] == "O" and not visited[i][j][0]:
                    # print(i,j ,'O') 
                    dfscheck(i,j)
                # print(surrounded)
                if not surrounded:
                    dfsassure(i,j)
                if surrounded and board[i][j] == "O" and visited[i][j][1] == 0:
                    dfsmarker(i, j)
                # print(i,j, board)
                # print(visited)
                
                surrounded = True
                
        
                




