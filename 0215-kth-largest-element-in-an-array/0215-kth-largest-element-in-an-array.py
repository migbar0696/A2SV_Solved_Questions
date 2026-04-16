class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freqn = Counter(nums)
        cnt = 0
        for i in range(10 **4, -(10**4 + 1), -1):
            cnt += freqn[i]
            if cnt >= k:
                return i