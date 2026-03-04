class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_pro = [1]
        suf_pro = [1]
        pro = 1
        for i in range(len(nums)):
            pro *= nums[i]
            pre_pro.append(pro)
        
        pro = 1
        for i in range(len(nums) - 1, -1, -1):
            pro *= nums[i]
            suf_pro.append(pro)
        # print(pre_pro, suf_pro)

        suf_pro.reverse()

        res = []
        for i in range(len(nums)):
            res.append(pre_pro[i ] * suf_pro[i + 1])
        
        return res
        

