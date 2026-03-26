class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(start, arr):
            if len(arr) >  len(nums):
                return 

            ans.append(arr[:])


            for i in range(start , len(nums)):

                arr.append(nums[i])
                
                backtrack(i + 1, arr)
                
                arr.pop()
            
            return ans
        
        return backtrack(0, [])

