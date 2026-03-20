class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n + 1)]
        self.cnt = 0
        self.n = n
        self.k = k

        def helper(arr1):

            if len(arr1) == 1:
                return arr1

            self.cnt += self.k - 1
            self.cnt = self.cnt % (len(arr1 ))
            arr1.remove(arr1[self.cnt ])
            
            helper(arr1)

            return arr1

        return helper(arr)[0]



            
