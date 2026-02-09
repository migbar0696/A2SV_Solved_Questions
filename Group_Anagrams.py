class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictan = defaultdict(list)

        for ele in strs:
            dictan["".join(sorted(ele))].append(ele)

        reslist = []
        for ele in dictan.values():
            reslist.append(ele)
        return reslist

            

        
