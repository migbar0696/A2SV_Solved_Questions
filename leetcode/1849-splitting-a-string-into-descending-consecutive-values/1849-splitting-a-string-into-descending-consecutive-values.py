class Solution:
    def splitString(self, s: str) -> bool:

        curr = []

        def backtrack(ind):

            if ind >= len(s):
                for i in range(1, len(curr)):
                    if curr[i - 1] - curr[i] != 1:
                        return False

                return len(curr) >= 2
            

            for i in range(ind, len(s)):
                curr.append(int(s[ind:i + 1]))

                if backtrack(i + 1):
                    return True

                curr.pop()
            
            return False
        
        return backtrack(0)


