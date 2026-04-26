class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        arr = [0] * k
        # print(arr)

        minv = float(inf)

        def backtrack(ind):
            # print(arr)
            nonlocal minv
            if ind >= len(cookies):
                minv = min(minv, max(arr))
                return 
            
            if max(arr) > minv:
                return

            
            for i in range(k):
                arr[i] += cookies[ind]

                backtrack(ind + 1)

                arr[i] -= cookies[ind]
        
        backtrack(0)
        return minv