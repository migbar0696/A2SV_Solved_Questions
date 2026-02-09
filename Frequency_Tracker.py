class FrequencyTracker:

    def __init__(self):
        self.mydict = {}
        self.dictfreq = {}

    def add(self, number: int) -> None:
        self.mydict[number] = self.mydict.get(number, 0) + 1
        
        self.dictfreq[self.mydict[number]] =  self.dictfreq.get(self.mydict[number], 0) + 1
        if self.mydict[number] > 1:
            self.dictfreq[self.mydict[number] - 1] -= 1

            if self.dictfreq[self.mydict[number] - 1] == 0:
                del self.dictfreq[self.mydict[number] - 1]

        print(number, self.dictfreq, "add")

    def deleteOne(self, number: int) -> None:
        if number in self.mydict.keys():

            if self.mydict[number] > 0:
                self.dictfreq[self.mydict[number] ] -= 1

                if self.mydict[number] > 1:
                    self.dictfreq[self.mydict[number] - 1 ] = self.dictfreq.get(self.mydict[number] - 1, 0) + 1

                if self.dictfreq[self.mydict[number]] == 0:
                    del self.dictfreq[self.mydict[number]]

            self.mydict[number] -= 1
            if self.mydict[number] == 0:
                del self.mydict[number]
            
            print(number, self.dictfreq, "del")



    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.dictfreq.keys():
            return True
        else:
            return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
