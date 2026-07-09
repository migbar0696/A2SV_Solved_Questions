class Solution:
    def minimumPushes(self, word: str) -> int:
        dictn = Counter(word)
        sortedict = dict(sorted(dictn.items(), key=lambda item:item[1], reverse = True))
        cnt = 0
        ans = 0
        print(dictn)
        print(len(dictn))
        for key, val in sortedict.items():
            ans += (((cnt // 8) + 1) * val)
            cnt += 1
        # print(sortedict)
        return ans