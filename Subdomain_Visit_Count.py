class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        

        from collections import defaultdict
        freqd = defaultdict(int)
        ans = []
        for dom in cpdomains:
            domain = dom.split()
            eachDomSplit = domain[1].split(".")
            tempans = []
            for i in range(len(eachDomSplit)):
                st = ""
                for j in range(i, len(eachDomSplit)):
                    st += eachDomSplit[j] + "."
                freqd[st[:-1]] += int(domain[0])
            
        for key, value in freqd.items():
            ans.append(f"{value} {key}")
        return ans
