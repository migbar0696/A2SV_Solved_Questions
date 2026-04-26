class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        curr = []

        self.res = []

        def backtrack(ind):
            if ind >= len(pattern):

                if len(curr) > len(pattern):
                    if self.res:
                        # print("".join(curr))
                        if int(self.res[-1]) > int("".join(curr)):
                            self.res = ["".join(curr)]
                    else:
                        self.res = ["".join(curr)]
                return



            if ind == -1:

                for i in range(len(num)):
                    curr.append(num[i])
                    backtrack(ind + 1)
                    curr.pop()
            else:

                for i in range(len(num)):
                    if pattern[ind] == "I":
                        if int(num[i]) > int(curr[-1]) and num[i] not in curr:
                            curr.append(num[i])
                            backtrack(ind + 1)
                            curr.pop()
                    elif pattern[ind] == "D":
                        if int(num[i]) < int(curr[-1]) and num[i] not in curr:
                            curr.append(num[i])
                            backtrack(ind + 1)
                            curr.pop()
            

            
        backtrack(-1)
        return self.res[0]

                        