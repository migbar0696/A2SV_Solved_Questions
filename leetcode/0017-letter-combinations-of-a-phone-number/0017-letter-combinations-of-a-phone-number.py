class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = []
        ans = []


        dictletters = {
            2:"abc",
            3: "def",
            4: "ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }

        def backtrack(ind, arr):
            if len(arr) == len(digits):
                ans.append("".join(arr[:]))
                return 
            
            if ind >= len(digits):
                return 

            
            for ch in dictletters[int(digits[ind])]:
                arr.append(ch)
                backtrack(ind + 1, arr)
                arr.pop()
            
            return ans
        
        return backtrack(0, [])



