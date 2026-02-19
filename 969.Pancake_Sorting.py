class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        res = []
        maxele = len(arr)

        for i in range(maxele):
            if arr.index(maxele) != maxele - 1:
                res.append(arr.index(maxele) + 1)
                res.append(maxele)
                
                arr[:arr.index(maxele) + 1 ] = arr[:arr.index(maxele) + 1 ][::-1]
                arr[:maxele ] = arr[:maxele ][::-1]
            maxele -= 1
        
        return res
