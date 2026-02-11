class Solution:
    def romanToInt(self, s: str) -> int:
        dictroman = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
            "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900 
        }

        sumn = 0

        i = 0
        while i < len(s):
            if  s[i] == "I":
                if s[i:i + 2] == "IV":
                    sumn += dictroman["IV"]
                    i += 2
                elif s[i:i + 2]  == "IX":
                    sumn += dictroman["IX"]
                    i += 2
                else:
                    sumn += dictroman["I"]
                    i += 1
            elif  s[i] == "X":
                if s[i:i + 2]  == "XL":
                    sumn += dictroman["XL"]
                    i += 2
                elif s[i:i + 2]  == "XC":
                    sumn += dictroman["XC"]
                    i += 2
                else:
                    sumn += dictroman["X"]
                    i += 1
            elif  s[i] == "C":
                if s[i:i + 2] == "CD":
                    sumn += dictroman["CD"]
                    i += 2
                elif s[i:i + 2]  == "CM":
                    sumn += dictroman["CM"]
                    i += 2
                else:
                    sumn += dictroman["C"]
                    i += 1
            elif s[i] == "V":
                sumn += dictroman["V"]
                i += 1
            elif s[i] == "L":
                sumn += dictroman["L"]
                i += 1
            elif s[i] == "D":
                sumn += dictroman["D"]
                i += 1
            elif s[i] == "M":
                sumn += dictroman["M"]
                i += 1

        return sumn
            
                
