class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []

        for strg in logs:
            if stack and strg == "../":
                stack.pop()
            
            if strg != "./" and strg != "../":
                stack.append(strg)
        
        return len(stack)