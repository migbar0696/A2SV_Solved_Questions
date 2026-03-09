from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        self.queue = deque()

    def consec(self, num: int) -> bool:
        self.queue.append(num)

        if num == self.value:
            self.count += 1
        
        if len(self.queue) > self.k:
            var = self.queue.popleft()

            if var == self.value:
                self.count -= 1
        
        return True if self.count == self.k else False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)