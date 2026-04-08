class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(leftarr, rightarr):
            
            lower = 0
            upper = 0
            arr = []
            while lower < len(leftarr) and upper < len(rightarr):
                if leftarr[lower] <= rightarr[upper]:
                    arr.append(leftarr[lower])
                    lower += 1
                else:
                    arr.append(rightarr[upper])
                    upper +=   1
            
            if lower < len(leftarr):
                arr.extend(leftarr[lower:])
            
            if upper < len(rightarr):
                arr.extend(rightarr[upper:])
            
            return arr


        
        def mergesort(left, right, arr):

            if left == right:
                return [arr[left]]
            
            mid = left + (right - left)//2 

            leftarr = mergesort(left, mid, arr)
            rightarr = mergesort(mid + 1, right, arr)

            return merge(leftarr, rightarr)
            
        return mergesort(0, len(nums) - 1, nums)