n, s = map(int, input().split())

listn = list(map(int, input().split()))

sumn = 0
nseg = 0
l = 0
for r in range(n):
    sumn += listn[r]
    
    while sumn >= s:
        nseg += n - r
        sumn -= listn[l]
        l += 1
print(nseg)

# or

# n, s = map(int, input().split())

# listn = list(map(int, input().split()))
# n = len(listn)
# sumw = 0
# l = 0
# ans = 0

# for r in range(n):
#     sumw += listn[r]
#     while sumw >= s:
#         sumw -= listn[l]
#         l += 1
#     ans += r - l + 1

# print( (n * (n + 1) // 2) - ans)
