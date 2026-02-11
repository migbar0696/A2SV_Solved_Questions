class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        freqn = Counter(nums)

        
        if any(freqn[key] >= 2 for key in freqn ):
            return True
        else:
            return False
