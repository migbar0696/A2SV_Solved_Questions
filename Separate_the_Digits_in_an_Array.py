class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        stlist = "".join(str(i) for i in nums) 

        return [int(j)  for j in stlist]
