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
