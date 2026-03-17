class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        maxpos = 0
        i = 0
        numpatch = 0
        
        while maxpos < n:
            if i < len(nums) and   maxpos + 1 >= nums[i]:
                maxpos += nums[i]
                i += 1
            else:
                numpatch += 1
                maxpos += maxpos + 1
        return numpatch
