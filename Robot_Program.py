from collections import Counter
t = int(input())


for i in range(t):
    n, x, k = map(int, input().split())
    pos = x
    stc = input()
    lrdict = Counter()
    cnt = 0
    flag = False
    flagequal = False
    for i in range(n):
        if stc[i] == "L":
            pos -= 1
            if pos == 0:
                flag = True
                break
                
        if stc[i] == "R":
            pos += 1
            if pos == 0:
                flag = True
                break
            
    lrdict[stc[0]] += 1
    j = 1
    while (j <  min(k - (i + 1), n )) and (lrdict["L"] != lrdict["R"] ):
        lrdict[stc[j]] += 1
        j += 1
    if flag and lrdict["L"]== lrdict["R"]:
        
        print(1 + (k - (i + 1)) // j)
    if flag and lrdict["L"] != lrdict["R"]:
        print(1)
    if not flag:
        print(0)
    
    
    
    
