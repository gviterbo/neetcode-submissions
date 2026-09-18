import bisect
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if not len(self.hm[key]):
            return ""
        index = bisect.bisect_left(self.hm[key], (timestamp,))
        if index >= len(self.hm[key]):
            return self.hm[key][-1][1]
        elif self.hm[key][index][0] == timestamp:
            return self.hm[key][index][1]
        elif index > 0:
            return self.hm[key][index-1][1]
        else:
            return ""
        
