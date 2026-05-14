import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
root = list(range(n + 1))
size = [1] *( n + 1)

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

finalcon = []

for _ in range(m):
    input()
op = []

for _ in range(k):
    a, b, c = input().split()
    op.append([a, int(b), int(c)])
ans = []
op.reverse()

for opr, b, e in op:
    if opr == "ask" and find(b) == find(e):
        ans.append("YES")

    elif opr == "ask":
        ans.append("NO")
    
    elif opr == "cut":
        union(b, e)

ans.reverse()

for each in ans:
    print(each)
        
