class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        leftcnt = 0
        rightcnt = 0
        longeststr = -1
        self.res = set()

        currstr = []

        def backtrack(ind):
            nonlocal leftcnt
            nonlocal rightcnt
            nonlocal longeststr

            if ind >= len(s):
                if leftcnt == rightcnt:

                    if len(currstr) > longeststr:
                        longeststr = len(currstr)
                        self.res = set()
                        self.res.add("".join(currstr))

                    elif len(currstr) == longeststr:
                        self.res.add("".join(currstr))
                return
            

            curr_ch = s[ind]

            if curr_ch == "(":
                currstr.append(curr_ch)
                leftcnt += 1
                backtrack(ind + 1)

                currstr.pop()
                leftcnt -= 1
                backtrack(ind + 1)
            elif curr_ch == ")":

                if leftcnt >  rightcnt:
                    currstr.append(curr_ch)
                    rightcnt += 1
                    backtrack(ind + 1)
                    rightcnt -= 1
                    currstr.pop()

                backtrack(ind + 1)
            else:
                currstr.append(curr_ch)
                backtrack(ind + 1)
                currstr.pop()
        backtrack(0)

        return list(self.res)
