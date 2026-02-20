n, k = map(int, input().split())

lista = list(map(int, input().split()))
difflist = []
for  i in range(n - 1):
    difflist.append(lista[i + 1] - lista[i])

mincost = 0
difflist.sort()

for i in range(n - k):
    mincost += difflist[i]
print(mincost)
