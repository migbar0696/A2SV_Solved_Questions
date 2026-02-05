class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        minlen = min(len(strs[0]), len(strs[-1]))
        res = []

        for i in range(minlen):
            if strs[0][i] == strs[-1][i]:
                res.append(strs[0][i])
            else:
                break
        return "".join(res)
