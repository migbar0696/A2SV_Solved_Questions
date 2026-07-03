class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        dictn = defaultdict(list)
        for i in range(len(groupSizes)):
            dictn[groupSizes[i]].append(i)
        
        ans = []
        temp = []
        cnt = 0
        for key, value in dictn.items():

            for num in value:
                cnt += 1
                temp.append(num)
                if cnt == key:
                    ans.append(temp)
                    temp = []
                    cnt = 0
        return ans