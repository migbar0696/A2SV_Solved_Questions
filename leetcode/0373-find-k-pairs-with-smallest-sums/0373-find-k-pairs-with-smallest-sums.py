class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        arr = []
        visited = set()
        ans = []
        n = len(nums1)
        m = len(nums2)

        heappush(arr, (nums1[0] + nums2[0], 0, 0))
        visited.add((nums1[0] + nums2[0], 0, 0))
        
        

        while len(ans) < k:
            num, col1, col2 = heappop(arr)
            ans.append([col1, col2])
            if col1 < n - 1 and  (nums1[col1 + 1] +  nums2[col2], col1+ 1, col2) not in visited:
                visited.add((nums1[col1 + 1] +  nums2[col2], col1+ 1, col2))
                heappush(arr, (nums1[col1 + 1] +  nums2[col2], col1+ 1, col2))

            if col2 < m - 1 and (nums1[col1 ] +  nums2[col2 + 1], col1, col2 + 1) not in visited:
                visited.add((nums1[col1 ] +  nums2[col2 + 1], col1, col2 + 1))
                heappush(arr, (nums1[col1 ] +  nums2[col2 + 1], col1, col2 + 1))
                # print(visited)
        return [ [nums1[x], nums2[y]] for x, y in ans ]
            

