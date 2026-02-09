class Solution:
    def intToRoman(self, num: int) -> str:
        
        dictroman = {
            1 : "I", 5 : "V", 10: "X", 50:"L", 100:"C", 500:"D", 1000:"M", 4: "IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"
        }

        n = len(str(num)) - 1
        listn = []
        for digit in str(num):
            num = int(digit) * (10 ** n)
            n -= 1 # don't forget to write break condition

            if num in dictroman:
                listn.append(dictroman[num])
            elif num >= 1000:
                st = ""
                while num >= 1000:
                    st += dictroman[1000]
                    num -= 1000
                listn.append(st)
            elif 500 <= num < 1000:
                st = "D"
                while num > 500:
                    st += dictroman[100]
                    num -= 100
                listn.append(st)
            elif 100 <= num < 500:
                st = ""
                while num >= 100:
                    st += dictroman[100]
                    num -= 100
                listn.append(st)
            elif 50 <= num < 100:
                st = "L"
                while num > 50:
                    st += dictroman[10]
                    num -= 10
                listn.append(st)
            elif  10 <= num < 50:
                st = ""
                while num >= 10:
                    st += dictroman[10]
                    num -= 10
                listn.append(st)
            elif 5 <= num < 10:
                st = "V"
                while num > 5:
                    st += dictroman[1]
                    num -= 1
                listn.append(st)
            elif 1 <= num < 5:
                st = ""
                while num >= 1:
                    st += dictroman[1]
                    num -= 1
                listn.append(st)
        return "".join(listn)
