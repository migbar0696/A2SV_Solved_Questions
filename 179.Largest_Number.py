class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            maxind = i
            for j in range(i, n):
                if int(str(nums[j])[0]) > int(str(nums[maxind])[0]):
                    maxind = j
                elif int(str(nums[j])[0]) == int(str(nums[maxind])[0]):
                    if int(str(nums[j]) + str(nums[maxind])) > int( str(nums[maxind]) + str(nums[j]) ):
                        maxind = j
                    
            nums[i], nums[maxind] = nums[maxind], nums[i]
        print("32" < "311")
        
        return str(int("".join(list(map(str, nums)))))
