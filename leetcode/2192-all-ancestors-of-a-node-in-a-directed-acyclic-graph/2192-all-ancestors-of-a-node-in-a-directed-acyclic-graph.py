class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        res = [set() for _ in range(n)]
        graph = [[] for _ in range(n)]
        incoming = [0 for _ in range(n)]
        queue = deque()

        for node1, node2 in edges:
            graph[node1].append(node2)
            incoming[node2] += 1
        
        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                incoming[neighbour] -= 1
                res[neighbour]= res[neighbour] | res[node]
                res[neighbour].add(node)

                if incoming[neighbour] == 0:
                    queue.append(neighbour)
        
        return [sorted(list(each)) for each in res]
        
        