class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        st = "abc"

        self.ans = []

        def backtrack(ind, arr):

            if len(arr) == n:
                self.ans.append( "".join(arr[:]))
                return
            

            for i in range(3):
                if arr:
                    if arr[-1] != st[i]:
                        arr.append(st[i])
                        backtrack(i + 1, arr)
                        arr.pop()
                else:
                    arr.append(st[i])
                    backtrack(i + 1, arr)
                    arr.pop()
        backtrack(0, [])
        return self.ans[k-1] if k <= len(self.ans) else ""