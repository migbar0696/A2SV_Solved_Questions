class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        lista = []

        for i in range(len(temperatures) - 1, - 1, - 1):

            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            if stack:
                lista.append(stack[-1][1] - i)
            else:
                lista.append(0)
            stack.append([temperatures[i], i])
        
        lista.reverse()

        return lista