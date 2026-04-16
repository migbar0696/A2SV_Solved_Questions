class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0,0]


        for num in nums:
            if nums[num - 1] < 0:
                res[0] = num
            else:
                nums[num - 1] *= -1
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res[1] = i + 1
            
        return res