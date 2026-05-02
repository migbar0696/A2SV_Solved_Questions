class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]

        for node1, node2 in edges:
            graph[node1].append(node2)
            indegree[node2] += 1
        
        ans = []
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                ans.append(i)
        
        return ans