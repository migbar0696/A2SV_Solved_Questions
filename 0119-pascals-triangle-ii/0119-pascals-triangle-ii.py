class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []

        for i in range(rowIndex + 1):
            rowresult = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    rowresult.append(1)
                
                else:
                    rowresult.append(res[i - 1][j - 1] + res[i - 1][j])
                
            res.append(rowresult)

        return res[rowIndex]
