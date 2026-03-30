class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mat = [["."] * n for i in range(n)]
        ans = []
        posDiag = set()
        negDiag = set()
        cols = set()

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in mat]
                ans.append(copy)
                return 
            

            for col in range(n):
                if col in cols or row + col  in posDiag or row - col in negDiag:
                    continue
                mat[row][col] = "Q"
                posDiag.add(row + col)
                negDiag.add(row - col)
                cols.add(col)

                backtrack(row + 1)

                mat[row][col] = "."
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                cols.remove(col)
        
        backtrack(0)
        return ans



