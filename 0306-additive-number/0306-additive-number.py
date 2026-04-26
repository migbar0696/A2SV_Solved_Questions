class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        flag = False

        curr = []

        def backtrack(ind):
            nonlocal flag

            if len("".join(curr)) >= len(num) or flag:
                # print("".join(curr), num)
                if len("".join(curr)) == len(num) and "".join(curr) == num and len(curr) > 2:
                    flag = True
                
                return

            if ind == 0:
                for i in range(ind, len(num)):
                    curr.append(str(int(num[ind:i + 1])))
                    for j in range(i + 1, len(num)):
                        curr.append(str(int(num[i + 1:j + 1])))
                        # print(curr)
                        backtrack(j + 1)
                        curr.pop()
                    curr.pop()
            
            else:
                newsum = str(int(curr[-2]) + int(curr[-1]))
                curr.append(newsum)
                backtrack(1)
                curr.pop()
    
        backtrack(0)

        return flag