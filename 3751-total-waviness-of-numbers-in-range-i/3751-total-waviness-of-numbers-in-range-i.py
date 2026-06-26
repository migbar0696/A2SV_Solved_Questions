class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        cnt = 0
        for num in range(num1, num2 + 1):
            for i in range(1, len(str(num)) - 1):
                if (int(str(num)[i]) > int(str(num)[i - 1])  and int(str(num)[i]) > int(str(num)[i + 1])  or (int(str(num)[i]) < int(str(num)[i - 1]))  and int(str(num)[i]) < int(str(num)[i + 1])):
                    cnt += 1
                    # print(int(str(num)[i]) , int(str(num)[i - 1]) ,  int(str(num)[i]) ,  int(str(num)[i + 1]))
                # print(int(str(num)[i]) , int(str(num)[i - 1]) ,  int(str(num)[i]) ,  int(str(num)[i + 1]))
                
        return cnt
                    
