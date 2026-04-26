class Solution:
    def totalNQueens(self, n: int) -> int:

        res = []

        curr = [["." for i in range(n)] for j in range(n)]
        
        # dn = [(1, 1), (1, -1), (1, 0)]
        setld = set()
        setrd = set()
        setc = set()

        def backtrack(row):

            if row == n  :
                res.append([''.join(each) for each in curr])
                return

            
        
            for col in range(n):
                if row - col not in setld and row + col  not in setrd and col not in setc:
                    setld.add(row - col)
                    setrd.add(row + col)
                    setc.add(col)
                    curr[row][col] = 'Q'

                    backtrack(row + 1)

                    curr[row][col] = '.'
                    setld.remove(row - col)
                    setrd.remove(row + col)
                    setc.remove(col)

        backtrack(0)
        return len(res)

