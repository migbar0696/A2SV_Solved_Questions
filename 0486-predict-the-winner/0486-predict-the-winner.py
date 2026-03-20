class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # self.flag = True
        self.max = 0

        if len(nums) == 1:
            return True

        def helper(nums):

            if len(nums) == 1:
                return nums[0]
            

            score1 = nums[0] - helper(nums[1:])
            score2 = nums[len(nums) - 1] - helper(nums[:len(nums) - 
           
            1])

            return max(score1, score2)
        
        if helper(nums) >= 0:
            return True




        
        return False



            
