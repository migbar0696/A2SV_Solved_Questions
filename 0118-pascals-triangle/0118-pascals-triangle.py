class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        temp = [1]
        ans = [[1]]
        for i in range(1, numRows):
            arr = [0] * (i + 1)
            for j in range( i + 1):
                if j - 1 >= 0:
                    arr[j] += temp[j - 1]
                    print(temp[j - 1])
                if j < i :
                    arr[j] +=temp[j]
                    print(temp[j])
            temp = arr.copy()
            ans.append(temp)
        return ans

        
