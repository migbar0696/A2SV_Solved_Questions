from collections import Counter
n, k = map(int, input().split())
listn = list(map(int, input().split()))

dictn = Counter()
ans = 0
l = 0

for r in range(n):
    dictn[listn[r]] += 1
    
    while  len(dictn) > k :
        dictn[listn[l]] -= 1
        
        if dictn[listn[l]] == 0:
            del dictn[listn[l]]
        l += 1
        
    ans += r - l + 1

print(ans)
    
