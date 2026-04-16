class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        freqn = Counter(nums)
        for key,  val in freqn.items():
            if val == 2:
                res.append(key)
        for i in range(1, len(nums) + 1):
            if i not in freqn.keys():
                res.append(i)
        
        return res