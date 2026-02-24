class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)

        l = 0
        r = len(people )- 1
        cnt = 0

        while  l <= r:
            if l == r:
                l += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                l += 1
            cnt += 1
        return cnt