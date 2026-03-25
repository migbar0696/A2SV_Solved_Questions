class Solution:
    def __init__(self):
        self.res = [1]
    def getRow(self, rowIndex: int) -> List[int]:


        def helper(res, rowIndex ):
            if rowIndex == 0:
                return self.res
            arr =  [0] * (len(res) + 1 )
            for i in range(len(arr) - 1):
                arr[i] += res[i]
                arr[i + 1] += res[i]
            self.res = arr.copy()
            helper(self.res, rowIndex - 1)
            return self.res

        return helper(self.res, rowIndex)

