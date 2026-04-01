class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        st = "abc"

        ans = []

        def backtrack(ind, arr):

            if len(arr) == n:
                ans.append( "".join(arr[:]))
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
        return ans[k-1] if k <= len(ans) else ""