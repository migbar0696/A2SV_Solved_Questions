class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []

        ni = 0
        pi = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                pi = i
                break

        for i in range(len(nums)):
            if nums[i] < 0:
                ni = i
                break
        for j in range(len(nums)//2):
            ans.append(nums[pi])
            ans.append(nums[ni])
            # print(ans)
            ni += 1
            while ni < len(nums) and nums[ni] > 0:
                ni += 1
            pi += 1
            while pi <len(nums) and nums[pi] < 0:
                pi += 1
        return ans
                