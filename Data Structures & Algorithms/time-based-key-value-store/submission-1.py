class TimeStamp:
    
    def __init__(self, val=None, time=None):
        self.val = val
        self.time = time
    
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_timestamp = TimeStamp(value, timestamp)
        self.time_map[key].append(new_timestamp)

    def get(self, key: str, timestamp: int) -> str:

        l, r = 0, len(self.time_map[key])
        
        # goal is to land on the val that is larger than timestamp then return the one before it that way we can get the largest meaning the val <= timestamp we are looking for
        while l < r:
            mid = (l + r) // 2

            if self.time_map[key][mid].time > timestamp:
                r = mid
            else: 
                l = mid + 1

        answer = l - 1
        return self.time_map[key][answer].val if answer >= 0 else ""


        # if the timestamp is > timestamp provided then we return ""
        
