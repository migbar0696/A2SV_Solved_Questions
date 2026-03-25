class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        ans = []
        for i in range( numRows):
            rowresult = []
            for j in range( i + 1):
                if j == 0 or j == i:
                    rowresult.append(1)
                else:
                    rowresult.append(res[i -1][j - 1] + res[i - 1][j])

            res.append(rowresult)

        return res

        
