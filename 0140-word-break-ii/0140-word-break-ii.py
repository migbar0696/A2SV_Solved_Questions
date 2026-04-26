class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        curr = ""

        currarr = []
        res = []

        cnt = 0
        def backtrack(ind):
            nonlocal curr
            nonlocal cnt
            cnt += 1
            print(cnt, ind,curr)
            if ind >= len(s):
                if len("".join(currarr)) == len(s):
                    # print(currarr)
                    res.append(" ".join(currarr)[:])
                
                return
            
            for i in range(ind, len(s)):
                curr += s[i]
                if curr in wordDict:
                    print(curr)
                    currarr.append(curr)
                    curr = ""
                    backtrack(i + 1)
                    curr = currarr.pop()
                     
        backtrack(0)
        return res

        