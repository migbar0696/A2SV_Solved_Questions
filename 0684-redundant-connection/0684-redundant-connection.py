class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges) + 1)]
        size = [1] *( len(edges) + 1)
        def find(x):

            if x == root[x]:
                return x
            
            root[x] = find(root[x])

            return root[x]

        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx == rooty:
                return True
            else:
                if size[rootx] > size[rooty]:
                    root[rooty] = rootx
                    size[rootx] += size[rooty]
                else:
                    root[rootx] = rooty
                    size[rooty] += size[rootx]
        
        for i, j in edges:
            if union(i, j):
                return i, j