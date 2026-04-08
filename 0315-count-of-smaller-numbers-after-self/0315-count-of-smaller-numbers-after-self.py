class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        def merge(leftarr, rightarr):

            left = 0
            right = 0
            arr  = []
            while left < len(leftarr) and right < len(rightarr):

                if leftarr[left][0] <= rightarr[right][0]:
                    arr.append(leftarr[left])
                    left += 1
                else:
                    arr.append(rightarr[right])
                    right += 1
                

            arr.extend(leftarr[left:])
            arr.extend(rightarr[right:])

            return arr

        def mergesort(left, right, arr):
            if left == right:
                return [[arr[left], left]]

            mid = left + (right - left)//2

            leftarr = mergesort(left, mid, nums)
            rightarr = mergesort(mid + 1, right, nums)
            for each in leftarr:
                ans[each[1]] += bisect_left(rightarr, [each[0], float(-inf)])


            return merge(leftarr, rightarr)
        
        mergesort(0, len(nums)-1, nums)
        return ans

