class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        from collections import defaultdict
        indexstr = defaultdict(list)
        setlist2 = set(list2)

        for ele in list1:
            if ele in setlist2:
                indexstr[list1.index(ele) + list2.index(ele)].append(ele)

        list_index = min(indexstr.keys())
        return indexstr[list_index]
        

