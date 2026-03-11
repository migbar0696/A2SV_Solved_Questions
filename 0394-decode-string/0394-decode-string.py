class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        numv = ""
        strv = ""
        nws = ""
        

        for i in range(len(s)):
            if s[i].isdigit():
                numv+=s[i]
            
            if s[i].isalpha():
                strv += s[i]
            
            if s[i] == "]" or s[i] == "[" or i == len(s) - 1:


                if numv != "" and strv != "":
                    stack.append(strv)
                    stack.append(numv)
                    numv = ""
                    strv = ""
                elif numv != "":
                    stack.append(numv)
                    numv = ""
                elif strv != "":
                    stack.append(strv)
                    strv = ""
            
            if s[i] == ']':

                v = len(stack) - 1
                while v >= 0 and stack[v].isalpha():
                    nws = stack[v] + nws
                    stack.pop()
                    v -= 1
                # print(nws)
                num = stack.pop()
                stack.append(int(num) * nws)
                nws = ""
        return "".join(stack)               


