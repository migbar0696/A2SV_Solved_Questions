class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freqn = Counter(nums)
        res = []
        n = len(nums)

        for key, value in freqn.items():
            if value > n/3 :
                res.append(key)
        
        return res

# second solution with O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freqele = defaultdict(int)
        res = []
        n = len(nums)

        for num in nums:
            freqele[num] += 1
            
            if len(freqele) == 3:
                for key in list(freqele.keys()):
                    freqele[key]  -= 1

                    if freqele[key] == 0:
                        del freqele[key]
        for key in freqele.keys():
            if nums.count(key)> n // 3:
                res.append(key)
        
        return res
        
