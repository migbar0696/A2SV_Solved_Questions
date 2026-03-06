class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        

        dictn = Counter([0])

        sumn = 0
        ans  = 0  
        for i in range(len(nums)):
            sumn += nums[i]
            ans += dictn[sumn % k] 

            dictn[sumn % k]  += 1
        
        return ans