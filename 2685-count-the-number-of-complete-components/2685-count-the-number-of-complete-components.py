class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = [False for _ in range(n)]
        graph = [[] for _ in range(n)]

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        cnt = 0

        notcomplete = False
        nodes = set()
        neighbous = set()

        def dfs(node):
            nonlocal notcomplete

            nodes.add(node)

            visited[node] = True
            for neighbour in graph[node]:
                    
                if not visited[neighbour] :
                   
                    dfs(neighbour)
                    if len(nodes) - 1  != len(graph[neighbour]):
                        notcomplete = True


        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                if not notcomplete:
                    cnt +=1
                
                notcomplete = False
                nodes = set()
        
        return cnt