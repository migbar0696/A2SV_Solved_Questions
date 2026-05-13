class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        size = [1] * len(isConnected)

        def find(x):

            while x != root[x]:
                root[x] = root[root[x]]

                x = root[x]
            return x
        
        def union(x, y):
            rootx , rooty = find(x), find(y)
            print(x, rootx, y, rooty)
            if rootx != rooty:
                if size[rootx] > size[rooty]:
                    root[rooty] = rootx
                    size[rootx] += size[rooty]
                else:
                    root[rootx] = rooty
                    size[rooty] += size[rootx]
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)
        for i in range(len(isConnected)):
                find(i)
        print(root)
        
        return len(set(root))
        