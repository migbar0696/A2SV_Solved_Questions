class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        pre_sum = [0] * (len(s) + 2)

        for start, end, val in shifts:
            
            if val == 1:
                pre_sum[start + 1] += 1
                pre_sum[end + 2] -= 1
            else:
                pre_sum[start + 1] -= 1
                pre_sum[end + 2] += 1

        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i] + pre_sum[ i - 1]

        ordl = [0] * (len(s) + 2)


        for i in range(len(s)):
            ordl[i + 1] = ord(s[i]) + pre_sum[i + 1]
        
        print(ordl)
        
        ans = []
        
        for i in range(1, len(s) + 1):
            ans.append(chr(ord("a") + ((ordl[i] - 97 ) % 26)))
        
        return "".join(ans)