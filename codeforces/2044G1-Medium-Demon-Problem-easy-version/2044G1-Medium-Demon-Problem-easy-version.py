import sys
input = sys.stdin.readline


from collections import deque
for i in range(int(input())):
    
    n = int(input())
    
    graph = [[] for _ in range(n + 1) ]
    
    listn = list(map(int,input().split()))
    # print(listn)
    indegree = [0 for _ in range(n + 1) ]
    queue = deque()
    for i in range( len(listn) ):
        graph[i + 1].append(listn[i])
        indegree[listn[i]] += 1
    
    # print(indegree)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            
    cnt = 0
    while queue:
        # print(queue)
        for _ in range(len(queue)):
            node = queue.popleft()
            
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
            
        cnt += 1
    print(cnt + 2)
            
    
    # print(graph)