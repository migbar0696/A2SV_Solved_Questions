class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0

        for each in nums:
            if each % 3:
                cnt += 1
        return cnt