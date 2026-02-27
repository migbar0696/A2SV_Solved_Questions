t = int(input())

for i in range(t):
    n = int(input())
    stra = input()
    strb = input()
    res = [0]
    
    if stra == strb:
        print("YES")
    else:
        
        cnt0 = 0
        cnt1 = 0
        
        for j in range(n):
            if stra[j] == "0":
                cnt0 += 1
            else:
                cnt1 += 1
            
            if cnt0 == cnt1:
                res.append(j + 1)
        
        for cnt in range(len(res) - 1):
            if stra[res[cnt]] == strb[res[cnt]]:
                if any(stra[i] != strb[i] for i in range(res[cnt], res[cnt + 1] , 1))  :
                    print("NO")
                    break
            else:
                if any(stra[i] == strb[i] for i in range(res[cnt], res[cnt + 1] , 1)) :
                    print("NO")
                    break
    
        else:
            if any(stra[i] != strb[i] for i in range(res[-1], n)):
                print("NO")
            else:
                print("YES")
        
        
