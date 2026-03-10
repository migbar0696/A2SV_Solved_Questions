class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        ans = []

        for i in range(len(nums2) - 1, -1, -1):
            
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            
            if not stack:
                ans.append(-1)
                stack.append(nums2[i])
            
            else:
                ans.append(stack[-1])
                stack.append(nums2[i])
        
        ans.reverse()

        
        dictn = defaultdict(int)

        for i in range(len(nums2)):
            dictn[nums2[i]] = ans[i]
        
        res = []

        for num in nums1:
            res.append(dictn[num])
        
        return res



