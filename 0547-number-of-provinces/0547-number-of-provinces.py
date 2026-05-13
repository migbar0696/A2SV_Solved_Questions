class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        size = [1] * len(isConnected)


        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootx , rooty = find(x), find(y)

            if rootx != rooty:
                if size[rootx] > size[rooty]:
                    root[rooty] = rootx
                    size[rootx] += size[rooty]
                else:
                    root[rootx] = rooty
                    size[rooty] += size[rootx]
        
        n = len(isConnected)
        numcomp = n

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1 and find(i) != find(j):
                    numcomp -= 1
                    union(i, j)
        
        return numcomp

                    

        