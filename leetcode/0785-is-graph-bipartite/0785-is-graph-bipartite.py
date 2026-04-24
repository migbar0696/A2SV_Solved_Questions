class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        

        color = [-1 for j in range(len(graph))]
        
        for i in range(len(graph)):

            if color[i] == -1:

                queue = deque([[i, 0]])
                color[i] = 0

                while queue:
                    node, colorn = queue.popleft()

                    for neighbour in graph[node]:
                        if color[neighbour]  != -1 and colorn == color[neighbour] :
                            return False
                        
                        elif color[neighbour] == -1:
                            color[neighbour] = 1 - colorn
                            queue.append([neighbour, 1-colorn])
            print(color)
        
        return True







