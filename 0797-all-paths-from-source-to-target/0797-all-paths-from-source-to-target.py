class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        ans = []
        def dfs(node):
            print(node)
            res.append(node)

            if node == len(graph) - 1:
                ans.append(res.copy())
                return 
            for each in graph[node]:
                dfs(each)
            
                res.pop()
        
        dfs(0)

        return ans
