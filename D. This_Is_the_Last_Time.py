t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    kcopy = k
    listn = []
    
    for j in range(n):
        listn.append(list(map(int, input().split())))
    
    listn.sort()
    
    for l, r, real in listn:
        if l <= kcopy <= r and kcopy < real:
            kcopy  = real
    
    print(kcopy) 
    
