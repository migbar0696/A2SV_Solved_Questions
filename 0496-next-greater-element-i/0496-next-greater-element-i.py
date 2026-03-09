class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for num in nums1:
            for j in range((nums2.index(num) + 1), len(nums2)):
                if nums2[j] > num:
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        
        return ans
            