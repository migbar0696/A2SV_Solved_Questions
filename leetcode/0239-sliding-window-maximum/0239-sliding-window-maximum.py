class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        queue = deque()
        ans = []
        for i in range(k):

            while queue and nums[i] > queue[-1]:
                queue.pop()
            
            queue.append(nums[i])

        ans.append(queue[0])

        for i in range(k, len(nums)):

            if queue and  nums[i - k] == queue[0]:
                queue.popleft()

            while queue and nums[i] > queue[-1]:
                queue.pop()
            
            queue.append(nums[i])

            ans.append(queue[0])
        
        return ans