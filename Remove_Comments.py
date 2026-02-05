class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        st = ""
        res = []
        flagbc = False 
        for ele in source:
                 # flag block line comment
            i = 0

            while i < len(ele):
                if not flagbc and ele[i:i + 2] == '/*':
                    flagbc = True
                    i += 2
                elif flagbc and ele[i:i + 2] == '*/':
                    flagbc = False
                    i += 2
                elif not flagbc and ele[i: i + 2] == '//':
                    break

                elif not flagbc:
                    st += ele[i]
                    i += 1
                else:
                    i += 1

            if not flagbc and st:
                res.append(st)
                st = ""
        return res
                
