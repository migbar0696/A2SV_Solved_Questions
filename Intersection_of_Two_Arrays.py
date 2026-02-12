class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        for ele in set(nums1):
            if ele in set(nums2):
                res.append(ele)
        
        return res
