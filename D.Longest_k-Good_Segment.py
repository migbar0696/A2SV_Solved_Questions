from collections import Counter
n, k = map(int, input().split())

dictn = Counter()
dictans = Counter()
maxl = 0
listn = list(map(int, input().split()))
l = 0

for r in range(len(listn)):
        dictn[listn[r]] += 1
        
        while len(dictn) > k:
            dictn[listn[l]] -= 1
            
            if dictn[listn[l]] == 0:
                del dictn[listn[l]]
                
            l += 1
        
        if r - l + 1 > maxl:
            dictans["r"] = r + 1
            dictans["l"] = l + 1
            
        maxl = max(maxl, r - l + 1)
print( dictans["l"], dictans["r"])
