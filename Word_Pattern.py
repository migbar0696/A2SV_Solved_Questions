class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict

        dictpattern = defaultdict(str)
        slist = s.split()
        n = len(slist)
        setused = set()

        if len(pattern) != len(slist):
            return False

        for i in range(n):
            if dictpattern[pattern[i]] != "" and dictpattern[pattern[i]] != slist[i] :
                return False
            elif dictpattern[pattern[i]] == "" and slist[i] not in setused:
                dictpattern[pattern[i]] = slist[i]
                setused.add(slist[i])
        
        if any(dictpattern[key] == "" for key in pattern):
            return False
        
        return True
