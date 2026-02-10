class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sumev = sum(num for num in nums if num % 2 == 0)

        for val, ind in queries:
            
            if (val + nums[ind]) % 2 == 0 and nums[ind] % 2:
                sumev += val + nums[ind]
            elif (val + nums[ind]) % 2 == 0 and nums[ind] % 2 == 0:
                sumev += val
            elif (val + nums[ind]) % 2  and nums[ind] % 2 == 0:
                sumev -= nums[ind]

            nums[ind] += val 
            
            answer.append(sumev)
        return answer
