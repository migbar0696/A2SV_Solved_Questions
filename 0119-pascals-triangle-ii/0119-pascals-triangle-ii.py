class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1, rowIndex + 1):
            arr = [0] * (i + 1)
            for j in range( i ):
                arr[j] += res[j]
                arr[j + 1]  = res[j]
            
            res = arr
        return res