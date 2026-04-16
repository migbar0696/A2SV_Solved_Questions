class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0,0]
        freqn = Counter(nums)

        for i in range(1, len(nums) + 1):
            if freqn[i] == 2:
                res[0] = i
            if freqn[i] == 0:
                res[1] = i
        
        return res