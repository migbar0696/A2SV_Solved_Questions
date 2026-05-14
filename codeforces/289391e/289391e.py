import sys
input = sys.stdin.readline

n, m = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)] 
        self.size = [1] * (n + 1)
        
    def find(self,x):
        if x == self.root[x]:
            return x
        
        self.root[x] =self.find(self.root[x])
        
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            
            if self.size[rootx] > self.size[rooty]:
                self.root[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.root[rootx] = rooty
                self.size[rooty] += self.size[rootx]
            
    
uf = UnionFind(n)
arr = []

for _ in range(m):
        arr.append(list(map(int, input().split())))


arr.sort(key=lambda x:x[2])
ans = 0

for b, e, w in arr:
    if uf.find(b) != uf.find(e):
        ans += w
        uf.union(b, e)
        
print(ans)