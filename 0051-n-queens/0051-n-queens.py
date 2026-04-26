class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        curr = [["." for i in range(n)] for j in range(n)]
        
        # dn = [(1, 1), (1, -1), (1, 0)]
        setld = set()
        setrd = set()
        setc = set()

        def backtrack(row, col):

            if row == n and  all("Q" in each for each in curr) :
                res.append([''.join(each) for each in curr])
                return

            
            for i in range(row, n):
                for j in range(n):
                    if i - j not in setld and i + j  not in setrd and j not in setc:
                        setld.add(i - j)
                        setrd.add(i + j)
                        setc.add(j)
                        curr[i][j] = 'Q'

                        backtrack(i + 1, j)

                        curr[i][j] = '.'
                        setld.remove(i - j)
                        setrd.remove(i + j)
                        setc.remove(j)

        backtrack(0, 0)
        return res

