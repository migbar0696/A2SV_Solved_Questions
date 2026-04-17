class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for num in nums:
            if abs(num) - 1 < len(nums) and abs(num) - 1 >= 0 and  nums[abs(num )- 1] >= 0 :
                print(nums[abs(num) - 1])
                if nums[abs(num ) - 1] == 0:
                    nums[abs(num) - 1] -= 2**31
                else:
                    nums[abs(num) - 1] *= -1
        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return len(nums) + 1

        