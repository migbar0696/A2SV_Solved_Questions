class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxw = float(-inf)

        l = 0
        r = len(height) - 1

        while l < r:
            maxw = max(maxw, min(height[l] , height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            elif height[l] == height[r]:
                if height[l + 1] > height[r - 1]:
                    l += 1
                else:
                    r -= 1
        return maxw