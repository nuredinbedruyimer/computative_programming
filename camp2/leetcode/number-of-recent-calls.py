class RecentCounter:

    def __init__(self):
        self.stack = deque()
        self.counter = 0

        

    def ping(self, t: int) -> int:
        while self.stack and t-self.stack[0]>3000:
            self.stack.popleft()
        if not self.stack or  t-self.stack[0]<=3000:
            self.stack.append(t)
        
        return len(self.stack)
            
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)