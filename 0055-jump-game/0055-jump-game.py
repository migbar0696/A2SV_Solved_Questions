class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxe = nums[0]
        for i in range(len(nums) - 1):

            if maxe == 0:
                return False
            maxe = max(maxe - 1, nums[i + 1])
        
        return True