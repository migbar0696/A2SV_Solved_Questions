class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        dictng = defaultdict(list)
        dictnl = defaultdict(list)
        moni = []
        mond = []
        stack = []

        for i in range(len(nums)):
            while moni and nums[i] <= moni[-1][0]:
                moni.pop()

            if moni and nums[i] > moni[0][0]:
                dictnl[i].append(moni[0][1])
        
            
            moni.append([nums[i], i])
        
        

            while mond and nums[i] >= mond[-1][0]:
                mond.pop()
            
            if mond:
                dictng[i].append(mond[-1][1])
            
            mond.append([nums[i], i])
        
        print(dictnl)
        print(dictng)
        

        for key, val in dictng.items():
            
            if dictnl[val[0]] and nums[key] > nums[dictnl[val[0]][0]]:
                return True

            
        
        
        # for key, val in dictn.items():
        #     if len(val) == 2 and val[1] > val[0]:
        #         return True
    
        
        
        return False
            
            