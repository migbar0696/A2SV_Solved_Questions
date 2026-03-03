n, k, q = map(int, input().split())

rec = []
qes = []
mins = float("inf")
maxe = 0
for i in range(n):
    start, end = map(int, input().split())
    rec.append([start, end])
    mins = min(mins, start)
    maxe = max(maxe, end)

    
for j in range(q):
    startq, endq = map(int, input().split())
    
    qes.append([startq, endq])
    mins = min(mins, startq)
    maxe = max(maxe, endq)

arr = [0] * ((maxe - mins) + 3)
arr1 = [0] * ((maxe - mins) + 3)

for start, end in rec:
    arr[start - (mins - 1)] += 1
    arr[end - mins + 2 ] -= 1


for i in range(1, len(arr)):
    arr[i] = arr[i - 1] + arr[i]

for i in range(len(arr)):
    if arr[i] >= k:
        arr1[i] = 1

for i in range(1, len(arr)):
    arr1[i] = arr1[i - 1] + arr1[i]


for start, end in qes:
    print(arr1[end - mins + 1] - arr1[start - mins])
    
