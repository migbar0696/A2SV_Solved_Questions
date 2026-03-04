t = int(input())

for i in range(t):
    n = int(input())
    listn = list(map(int, input().split()))
    m = int(input())
    listm = list(map(int, input().split()))
    
    def solve(n, listn):
        
        maxn = float("-inf")
        sumn = 0
        for i in range(n):
            sumn += listn[i]
            
            maxn = max(maxn, sumn)
        return maxn if maxn > 0 else 0

    print(solve(n, listn) + solve(m, listm))
        
        
