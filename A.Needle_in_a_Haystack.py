from collections import Counter
t = int(input())

for i in range(t):
    
    sst = input()
    tst = input()
    
    tfreq = Counter(tst)
    sfreq = Counter(sst)
    res = []
    tstleft = []
    
    if all(sfreq[key] <= tfreq[key] for key in sst):
        for key in sfreq.keys():
            tfreq[key] -= sfreq[key]
        
        sortedtst = sorted(tfreq.keys())
        up = 0
        lw = 0
        
        for key in sortedtst:
            for j  in range(tfreq[key]):
                tstleft.append(key)

        while up < len(sst) and lw < len(tstleft):
            if sst[up] <= tstleft[lw]:
                res.append(sst[up])
                up += 1
            else:
                res.append(tstleft[lw])
                lw += 1
        
        res.extend(sst[up:])
        res.extend(tstleft[lw:])
                
        print("".join(res))
    else:
        print("Impossible")
    
        
    
    
