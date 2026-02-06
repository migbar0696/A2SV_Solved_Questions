class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ansdict = defaultdict(list)
        finalans = []

        for path in paths:
            pathlist = path.split()

            for i in range(1, len(pathlist)):
                flagop = False
                strb = ''
                stra = ''
                for j in range(len(pathlist[i])):
                    if pathlist[i][j] == '(':
                        flagop = True

                    if flagop and pathlist[i][j] != '('and pathlist[i][j] != ')':
                        stra += pathlist[i][j]

                    if not flagop:
                        strb += pathlist[i][j]
                    
                ansdict[stra].append(pathlist[0]+"/" + strb)
        
        for key in ansdict.keys():
            if len(ansdict[key]) >= 2:
                finalans.append(ansdict[key])
        return finalans
