class Solution:
    def sortVowels(self, s: str) -> str:
        listn = []
        vowel = ["a", "e", "i", "o", "u"]

        for each in s:
            if each.lower() in vowel:
                listn.append(each)
        listn.sort()
        
        ans = []
        cnt = 0
        for each in s:
            if each.lower() in vowel:
                ans.append(listn[cnt])
                cnt += 1
            else:
                ans.append(each)
        return "".join(ans)