t = int(input())
from collections import Counter
for i in range(t):
    n, k = map(int, input().split())
    strc = input()
    
    dictst = Counter(strc[:k])
    minc = dictst["W"]
    l = 0
    for r in range(k, len(strc)):
        dictst[strc[r]] += 1
        dictst[strc[l]] -= 1
        l += 1
        minc = min(minc, dictst["W"])
    
    print(minc)

