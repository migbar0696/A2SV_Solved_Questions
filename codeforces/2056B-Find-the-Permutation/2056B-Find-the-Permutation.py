import sys
input = sys.stdin.readline
from collections import defaultdict

for i in range(int(input())):
    n = int(input())
    admat = []
    graph = defaultdict(list)
    graph2 = defaultdict(list)
    for j in range(n):
        row = list(map(int, list(input().strip())))
        # print(row)
        for k in range(len(row)):
            if row[k] == 1 :
                graph[j + 1].append(k + 1)
            elif k != j:
                graph2[j + 1].append(k + 1)
        
    res = []
    for node in range(1, n + 1):
        left , right = 0, 0
        
        for each in graph[node]:
            if each > node:
                right += 1
            else:
                left += 1
        
        for each in graph2[node]:
            if each > node:
                left += 1
            else:
                right += 1
        res.append(left)
    # print(res, len(res))
    
    ans = [0] * n
    
    for i in range(n):
        ans[res[i] ] = i + 1
    
    print(*ans)
        
            
                     
            
        
        
    
    # print(graph, graph2)