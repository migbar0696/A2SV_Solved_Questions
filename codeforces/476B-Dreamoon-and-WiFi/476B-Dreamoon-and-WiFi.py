def backtrack(ind, ans):
    if ind >= len(s2):
        reslist.append(ans)
        return
    
    if s2[ind] == "+":
        
        backtrack(ind + 1, ans + 1)
    elif s2[ind] == "-":
        backtrack(ind + 1, ans - 1)
        
    else:
        backtrack(ind + 1, ans + 1)
        backtrack(ind + 1, ans- 1)
        
backtrack(0, 0)
print(reslist.count(ans)/ len(reslist))