class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
 
        ans = 0
        l = 0
        r = len(skill) - 1
        n = len(skill ) 
        target = sum(skill) // (n // 2)
        while l < r:
            if target != skill[l] + skill[r]:
                return -1
            ans += (skill[l] * skill[r])
            l += 1
            r -= 1

        return ans
