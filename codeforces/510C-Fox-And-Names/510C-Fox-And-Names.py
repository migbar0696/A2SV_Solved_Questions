import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())

stlist =[]
graph = defaultdict(list)

for _ in range(n):
    stlist.append(input().strip())
# print(stlist)

flag = True

setch = set()

for i in range(n -1):
    if stlist[i + 1] in stlist[i][:len(stlist[i + 1]) ]:
        flag = False
        break

indegree = defaultdict(int)
queue = deque()
if flag:
    for i in range(n - 1):
        for j in range(min(len(stlist[i]), len(stlist[i + 1]))):
            if stlist[i][j] != stlist[i + 1][j]:
                graph[stlist[i][j]].append(stlist[i + 1][j])
                indegree[stlist[i+ 1][j]] += 1
                break
    
    for i in range(97, 123):
        
        if indegree[chr(i)] == 0:
            queue.append(chr(i))
    # print(queue, indegree["p"])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
        
    # print(len(order), len(graph))
    if len(order) == 26:
        print("".join(order))
        
    else:
        print("Impossible")
else:
    print("Impossible")