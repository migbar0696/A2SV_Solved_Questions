class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        total = 0
        score = 0
        stack = []

        for par in s:

            if par == "(":
                stack.append(0)
                # print(stack)
            else:

                num = stack.pop()

                if num == 0:
                    score = 1
                else:
                    score = 2 * num
            
                
                if stack:
                    stack[-1] += score
                else:
                    total += score
        
        return total