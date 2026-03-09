from collections import deque
class RecentCounter:

    def __init__(self):
        self.count = 0
        self.queue = deque()

    def ping(self, t: int) -> int:

        while self.queue and self.queue[0] < t - 3000:
            self.count -= 1
            self.queue.popleft()
        
        self.queue.append(t)
        self.count += 1

        return self.count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)