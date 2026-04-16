class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0,0]


        for num in nums:
            if nums[abs(num) - 1] < 0:
                res[0] = abs(num)
            else:
                nums[abs(num) - 1] *= -1


        for i in range(len(nums)):
            if nums[i] > 0:
                res[1] = i + 1
            
        return res