
n = int(input())
contestn = sorted(list(map(int, input().split())))
nlen = len(contestn)
cnt = 0
for i in range(nlen):
    if cnt + 1 <= contestn[i]:
        cnt += 1
        
print(cnt)
