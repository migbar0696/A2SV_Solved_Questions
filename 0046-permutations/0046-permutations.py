class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        curr = []
        res = []

        def backtrack(ind):

            if len(curr) == len(nums):
                res.append(curr[:])
            

            for i in range(len(nums)):

                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(i + 1)
                    curr.pop()

        backtrack(0)
        return res