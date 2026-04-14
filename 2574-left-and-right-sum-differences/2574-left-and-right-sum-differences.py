class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        sumn = 0
        leftsum = []

        for i in range(len(nums) ):
            leftsum.append(sumn)
            sumn += nums[i]
        

        sumn = 0
        rightsum = []
        nums.reverse()
        for i in range(len(nums) ):
            rightsum.append(sumn)
            sumn += nums[i]
        
        rightsum.reverse()
        print(rightsum)

        res = []
        for i in range(len(rightsum)):
            res.append(abs(leftsum[i] - rightsum[i]))
        
        return res
        
        
