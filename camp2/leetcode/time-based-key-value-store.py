class TimeMap(object):

    def __init__(self):
        self.memo = dict()

    def set(self, key, value, timestamp):
        if not key in self.memo:
            self.memo[key] = []
        self.memo[key].append([timestamp, value])
        

    def get(self, key, timestamp):
        if not key in self.memo:
             return ""
        left = 0

        right = len(self.memo[key]) - 1

        pos = -1
        while left <= right:

            mid = (left+right) // 2

            if self.memo[key][mid][0] <= timestamp:
                  left = mid + 1
                  pos = mid
            else:
                  right = mid - 1
        if pos == -1: 
            return ""
        return self.memo[key][pos][1]
