t = int(input())

for i in range(t):
    n = int(input())
    listn = list(map(int, input().split()))
    res = [listn[0]]
    for i in range(1, len(listn) - 1):
        if (listn[i] > listn[i - 1]  and listn[i] > listn[i + 1]) or (listn[i] < listn[i - 1]  and listn[i] < listn[i + 1]):
            res.append(listn[i])
    
    res.append(listn[-1])
    
    print(len(res))
    print(*res)
