class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        dictn = Counter([0])

        sumn = 0
        ans = 0

        for i in range(len(nums)):
            sumn += nums[i]

            ans += dictn[sumn - goal]

            dictn[sumn] += 1
        
        return ans