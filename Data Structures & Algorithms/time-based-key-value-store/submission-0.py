from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.hashMap[key]) - 1
        res = ''
        while l <= r:
            middle = l + (r-l)//2
            pair = self.hashMap[key]

            if pair[middle][0] == timestamp:
                return pair[middle][1]
            elif pair[middle][0] > timestamp:
                r = middle - 1
            else:
                res = pair[middle][1]
                l = middle + 1                
        return res
        
