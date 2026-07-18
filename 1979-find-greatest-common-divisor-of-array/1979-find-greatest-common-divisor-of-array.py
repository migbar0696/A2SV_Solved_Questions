class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn = min(nums)
        maxn = max(nums)
        sets = set()
        setl = set()
        num = 1

        for i in range(1, maxn + 1):
            if minn % i == 0 and maxn % i == 0:
                num = max(num, i)
                


        return num
